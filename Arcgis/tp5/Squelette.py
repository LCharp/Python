# -*- coding: cp1252 -*-

# Ce script est celui de l'outil de script "Squelettisation".
# Cet outil poss�de 2 param�tres :
# le polygone � squelettiser (en entr�e) et le squelette obtenu (en sortie).
# Il y a quelques modifications � faire au d�but de script.
# Elles sont indiqu�es en commentaire.

import arcpy

#Polygone_entrant = 'Tampon' # Remplacer par
Polygone_entrant = arcpy.GetParameterAsText(0)
#Squelette_sortant = 'Squelette' # Remplacer par
Squelette_sortant = arcpy.GetParameterAsText(1)

# Il n'y a plus de modification � faire.

spref = arcpy.Describe(Polygone_entrant).spatialReference

curseur = arcpy.SearchCursor(Polygone_entrant)
ligne = curseur.next()
del curseur

geom = ligne.Shape
del ligne

xmin = geom.extent.XMin
xmax = geom.extent.XMax
ymin = geom.extent.YMin
ymax = geom.extent.YMax
xmax = xmax - xmin
ymax = ymax - ymin

pts = arcpy.Array()
for i in range(geom.partCount):
    pts.extend(geom.getPart(i))

# Purification
import math
d = math.sqrt(xmax*xmax + ymax*ymax)/100
i = 0
while i < len(pts)-1:
    x1, y1 = pts[i].X, pts[i].Y
    x2, y2 = pts[i + 1].X, pts[i + 1].Y
    dd = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    if dd < d:
        pts.remove(i+1)
        i -= 1
    i = i+1

# Compl�tion
i = 0
while i < len(pts)-1:
    x1, y1 = pts[i].X, pts[i].Y
    x2, y2 = pts[i + 1].X, pts[i + 1].Y
    dd = math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    if dd > 2*d:
        n = int(dd/d)
        dx, dy = (x2 - x1)/n, (y2 - y1)/n
        for ii in range(n - 1):
            x = x1 + (ii + 1.0) * dx
            y = y1 + (ii + 1.0) * dy
            i += 1
            pts.insert(i,arcpy.Point(x, y))
    i += 1

pts.remove(len(pts) - 1) # le dernier point est identique au 1er.

nbpts = len(pts)

coordonnees = []
for pt in pts:
    coordonnees.append([pt.X - xmin, pt.Y - ymin])
del pt, pts

noeuds = [] # [x,y,i,j,k] Les noeuds du squelette

zero = d / 1000.
for i in range(nbpts - 2):
    x1, y1 = 0.0 + coordonnees[i][0], 0.0 + coordonnees[i][1]
    for j in range(i + 1,nbpts - 1):
        x2, y2 = 0.0 + coordonnees[j][0], 0.0 + coordonnees[j][1]
        for k in range(j + 1, nbpts):
            x3, y3 = 0.0 + coordonnees[k][0], 0.0 + coordonnees[k][1]
            d = 0.0 + (x3-x2)*(y3-y1)-(x3-x1)*(y3-y2)
            if (d > - zero) and (d < zero):
                continue
            dx = 0.0 + ((x3*x3+y3*y3-x2*x2-y2*y2)*(y3-y1)-(x3*x3+y3*y3-x1*x1-y1*y1)*(y3-y2))/2
            x = dx/d
            if(x > xmax) or (x < 0):
                continue
            dy = 0.0 + ((x3-x2)*(x3*x3+y3*y3-x1*x1-y1*y1)-(x3-x1)*(x3*x3+y3*y3-x2*x2-y2*y2))/2
            y = dy/d
            if(y > ymax) or (y < 0):
                continue
            d = 0.0 + (x1-x)*(x1-x) + (y1- y)*(y1- y)
            bon = True
            for ii in range(nbpts):
                if ii != i and ii != j and ii != k:
                    d_ = 0.0 + (coordonnees[ii][0]-x)*(coordonnees[ii][0]-x)\
                    + (coordonnees[ii][1]-y)*(coordonnees[ii][1]-y)
                    bon = (d_ >= d)
                    if not bon:
                        break
            if bon:
                noeuds.append([x, y, i, j, k])

nbnoeuds = len(noeuds)

geoms = []
pt = arcpy.Point()
for i in range(nbnoeuds):
    pt.X, pt.Y = noeuds[i][0] + xmin, noeuds[i][1] + ymin
    ptgeom = arcpy.PointGeometry(pt, spref)
    geoms.append(ptgeom)

cible = arcpy.Geometry()
sommets = arcpy.Clip_analysis(geoms,geom,cible)

del geoms, cible

noeuds2 = [] # [pt, i, j, k, voisins, fin] Encore les noeuds du squelette
for ptgeom in sommets:
    pt = ptgeom.firstPoint
    for i in range(nbnoeuds):
        if int(pt.X) == int(noeuds[i][0] +xmin) and int(pt.Y) == int(noeuds[i][1] +ymin):
            break
    noeud = noeuds[i]
    pt_ = arcpy.Point(noeud[0] + xmin,noeud[1] + ymin)
    noeuds2.append([pt_,noeud[2],noeud[3], noeud[4],0,False])
del noeuds, pt
nbnoeuds = len(noeuds2)

for i in range(nbnoeuds - 1):
    for j in range (i + 1, nbnoeuds):
        if len(set(noeuds2[i][1:4])|set(noeuds2[j][1:4])) == 4:
            noeuds2[i][4] += 1
            noeuds2[i][5] = noeuds2[i][4] > 2
            noeuds2[j][4] += 1
            noeuds2[j][5] = noeuds2[j][4] > 2

# Suppression des noeuds isol�s
i = 0
while i < len(noeuds2):
    if noeuds2[i][4] == 0:
        noeuds2.pop(i)
        i -= 1
    i += 1
nbnoeuds = len(noeuds2)

tiges = [] # Les lignes du squelette.
encore_tige = False

paires = []

voisins = 10
n1 = -1
for n in range(nbnoeuds):
    if noeuds2[n][4] < voisins:
        n1 = n
        voisins = noeuds2[n][4]
encore_tige = (n1 > -1)

pts = arcpy.Array()
total = 0
while encore_tige:
    pts.append(noeuds2[n1][0])
    encore_pt = False
    for n2 in range(len(noeuds2)):
        if len(set(noeuds2[n1][1:4])|set(noeuds2[n2][1:4])) == 4:
            paire = set((noeuds2[n1][0],noeuds2[n2][0]))
            if paire not in paires:
                paires.append(paire)
                encore_pt = True
                break

    while encore_pt:
        pts.append(noeuds2[n2][0])
        noeuds2[n1][4] -= 1
        if noeuds2[n1][4] == 0:
            noeuds2.pop(n1)
            if n2 > n1:
                n2 -= 1

        noeuds2[n2][4] -= 1
        if noeuds2[n2][5]: # Fin de la tige
            if noeuds2[n2][4] == 0:
                noeuds2.pop(n2)
            break
        if noeuds2[n2][4] == 0:
            noeuds2.pop(n2)
            break
        n1 = n2
        encore_pt = False
        for n2 in range(len(noeuds2)):
            if len(set(noeuds2[n1][1:4])|set(noeuds2[n2][1:4])) == 4:
                paire = set((noeuds2[n1][0],noeuds2[n2][0]))
                if paire not in paires:
                    paires.append(paire)
                    encore_pt = True
                    break

    for n in range(1): # Lissage. Choisir le niveau de lissage.
        for i in range(len(pts) - 2):
            mobile = True
            for tige in tiges:
                if pts[i+1] == tige.lastPoint:
                    mobile = False
                    break
            if not mobile:
                continue
            x1, y1 = pts[i].X, pts[i].Y
            x2, y2 = pts[i+1].X, pts[i+1].Y
            x3, y3 = pts[i+2].X, pts[i+2].Y
            d = (x3 - x1) * (x3 - x1) + (y3 - y1) * (y3 - y1)
            if d == 0:
                continue
            s = (x3 - x1) * (x2 - x1) + (y3 - y1) * (y2 - y1)
            x, y = x1 + (x3 - x1) * s / d, y1 + (y3 - y1) * s / d
            pts[i+1].X, pts[i+1].Y = x, y

    tiges.append(arcpy.Polyline(pts,spref))
    total += len(pts)
    pts.removeAll()

    voisins = 10
    n1 = -1
    for n in range(len(noeuds2)):
        if noeuds2[n][4] < voisins:
            n1 = n
            voisins = noeuds2[n][4]
    encore_tige = (n1 > -1)

del pts, paires, noeuds2

# Suppression des tiges trop courtes
nb,lg = 0,0.0
for tige in tiges:
    nb += 1
    lg += tige.length
lg = lg / nb / 10
i = 0
while i < len(tiges):
    if tiges[i].length < lg:
        tiges.pop(i)
        i -= 1
    i += 1

arcpy.CopyFeatures_management(tiges,Squelette_sortant)

del tiges
