import arcpy
class ToolValidator(object):
  """Class for validating a tool's parameter values and controlling
  the behavior of the tool's dialog."""
  global blocs
  global mxd
  global couches
  def __init__(self):
    """Setup arcpy and the list of tool parameters."""
    import arcpy
    self.params = arcpy.GetParameterInfo()
    mxd = arcpy.mapping.MapDocument("CURRENT") # Document
    blocs = arcpy.mapping.ListDataFrames(mxd)
    couches = arcpy.mapping.ListLayers(mxd)

  def initializeParameters(self):
    """Refine the properties of a tool's parameters.  This method is
    called when the tool is opened."""
    mxd = arcpy.mapping.MapDocument("CURRENT") # Document
    blocs = arcpy.mapping.ListDataFrames(mxd)
    couches = arcpy.mapping.ListLayers(mxd)
    liste = []
    for bloc in blocs:
        liste.append(bloc.name)
    self.params[0].filter.list = liste
    return
  def updateParameters(self):
    """Modify the values and properties of parameters before internal
    validation is performed.  This method is called whenever a parameter
    has been changed."""
    mxd = arcpy.mapping.MapDocument("CURRENT") # Document
    blocs = arcpy.mapping.ListDataFrames(mxd)
    couches = arcpy.mapping.ListLayers(mxd)
    liste = []
    for bloc in blocs:
        liste.append(bloc.name)
    self.params[0].filter.list = liste
    if self.params[0].altered:
	i=0
	bloc= blocs[i]
	while self.params[0].value != blocs[i].name:
		i +=1
		bloc = blocs[i]
        couches = arcpy.mapping.ListLayers(mxd,"",bloc) # Liste des couches
	liste = []
	for couche in couches:
		liste.append(couche.name)
	self.params[1].filter.list = liste
    if self.params[1].altered:
	i=0
	couche= couches[i]
	while self.params[1].value != couches[i].name:
		i +=1
		couche = couches[i]
	fc = couche.dataSource # FeatureClass associée à la couche
	global champs
	champs = arcpy.ListFields(fc) # Liste des champs
	liste = []
	for champ in champs:
		liste.append(champ.name)
	self.params[2].filter.list = liste
    return

  def updateMessages(self):
    """Modify the messages created by internal validation for each tool
    parameter.  This method is called after internal validation."""
    return
