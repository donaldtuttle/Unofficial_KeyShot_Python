# Keyshot Python3.11 Lux

```python
KeyShot 2023.2 Python Scripting Documentation
built-in module lux

lux          index (built-in)

CLASSES
    builtins.object
        ColorParameter
        Colorway
        Env
        ImageStyle
        MaterialGraph
        MaterialMetadata
        MultiMaterial
        RenderOptions
        SceneNode
        ShaderEdge
        ShaderNode
        ShaderParameter
        Studio
        ThumbnailRenderOptions
    
    class ColorParameter(builtins.object)
       TODO
       
       Methods defined here:
       
       __hash__(self, /)
           Return hash(self).
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       getActiveSubColor(...)
           Gets the currently active sub color. Can only be called on multi colors!
       
       getColor(...)
           Get RGBA color value.
       
       getName(...)
           Get name of color.
       
       getSubColors(...)
           Gets the list of sub colors. Can only be called on multi colors!.
       
       isMultiColor(...)
           Is it a multi color.
       
       setActiveSubColor(...)
           Sets the currently active sub color. Must be part of the sub colors!
           sub = The sub color to activate. *
       
       setCMYK(...)
           Set value of color.
           color = 4 numbers in range [0,100]. *
       
       setHSV(...)
           Set value of color.
           color = 3 numbers in range [0,360[, [0,100], [0,100]. *
       
       setHex(...)
           Set value of color.
           color = Hexadecimal string representing the RGB color. *
       
       setKelvin(...)
           Set value of color.
           color = Kelvin temperature in range [2500,9500]. *
       
       setLab(...)
           Set value of color.
           color = 3 numbers in range [0,100], [-128,128], [-128,128]. *
       
       setName(...)
           Set color name. Names must be unique!
           name = The requested name. *
       
       setRGBA(...)
           Set RGB(A) value of color.
           color = 3 or 4 numbers in range [0,255]. *
       
       setRGBAf(...)
           Set RGB(A) value of color.
           color =  3 or 4 numbers in range [0,1]. *
       
       setSubColors(...)
           Sets the list of sub colors. The order matters. Can only be called on multi colors!
           colors = The list of sub colors. *
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class Colorway(builtins.object)
       TODO
       
       Methods defined here:
       
       __hash__(self, /)
           Return hash(self).
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       appendColor(...)
           Append a multi/sub color to colorway.
           multi = The multi color to append.
           sub = The sub color to append. Must be part of the multi color!*
       
       getColors(...)
           Get colors of colorway.
       
       getName(...)
           Get name of colorway.
       
       removeColor(...)
           Remove a multi color from colorway.
           color = The multi color to remove. *
       
       setName(...)
           Set colorway name. Names must be unique!
           name = The requested name. *
       
       updateColor(...)
           Update a multi color from colorway.
           multi = The multi color to update.
           sub = The sub color to activate. Must be part of the multi color!*
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class Env(builtins.object)
       Env encapsulates environment settings in a clear and consise way. Get an instance of the active environment using lux.getActiveEnvironment().
       
       Methods defined here:
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       getBackgroundColor(...)
           Get background color as an RGB tuple.
       
       getBackplateImage(...)
           Get backplate image, if set.
       
       getBrightness(...)
           Get environment brightness in the form of a float value.
       
       getFlattenGround(...)
           Returns whether flattening of the ground is enabled or disabled.
       
       getGroundReflections(...)
           Returns whether ground reflections are enabled or disabled.
       
       getGroundShadows(...)
           Returns whether ground shadows are enabled or disabled.
       
       getGroundShadowsColor(...)
           Get ground shadows color as an RGB tuple.
       
       getGroundSize(...)
           Get environment ground size.
       
       getHeight(...)
           Get environment height.
       
       getLightingEnvironment(...)
           Get the environment image.
       
       getName(...)
           Get environment name.
       
       getOcclusionGroundShadows(...)
           Returns whether occlusion ground shadows are enabled or disabled.
       
       getRotation(...)
           Get environment rotation.
       
       getSize(...)
           Get environment size.
       
       setBackgroundColor(...)
           Apply RGB color as the background color.
           color = RGB color tuple. *
       
       setBackplateImage(...)
           Applies backplate image to the scene.
           path = Path to or base name of the backplate image. *
       
       setBrightness(...)
           Set environment brightness.
           value = Brightness value to set in the form of a float. *
       
       setFlattenGround(...)
           Enable or disable flattening of the ground.
           enable = Boolean value for enabling or disabling flattening of the ground. *
       
       setGroundReflections(...)
           Enable or disable ground reflections.
           enable = Boolean value for enabling or disabling ground reflections. *
       
       setGroundShadows(...)
           Enable or disable ground shadows.
           enable = Boolean value for enabling or disabling ground shadows. *
       
       setGroundShadowsColor(...)
           Apply RGB color as the ground shadows color.
           color = RGB color tuple. *
       
       setGroundSize(...)
           Set environment ground size.
           size = Environment ground size in the form of a number larger than zero (in meters). *
       
       setHeight(...)
           Set environment height.
           height = Environment height in the form of a float value in [-0.5, 0.5]. *
       
       setLightingEnvironment(...)
           Applies an image as the scene's lighting environment. When no path is specified then current lighting environment is used, which is useful when switching from backplate or color background to lighitng environment.
           path = Path to or base name of the environment image to apply. *
       
       setOcclusionGroundShadows(...)
           Enable or disable occlusion ground shadows. It is only possible when ground shadows are enabled.
           enable = Boolean value for enabling or disabling occlusion ground shadows. *
       
       setRotation(...)
           Set environment rotation.
           rotation = Environment rotation in the form of a float value in [0, 360[. *
       
       setSize(...)
           Set environment size.
           size = Environment size in the form of a number value in meters. *
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class ImageStyle(builtins.object)
       ImageStyle encapsulates image style settings in a clear and consise way. Get an instance of the active image style using lux.getActiveImageStyle().
       
       Methods defined here:
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       getBloom(...)
           Returns whether bloom is enabled or disabled for the image style.
       
       getChromaticAberration(...)
           Returns whether chromatic aberration is enabled or disabled for the image style.
       
       getColor(...)
           Returns whether color is enabled or disabled for the photographic image style.
       
       getCurve(...)
           Returns whether curve is enabled or disabled for the photographic image style.
       
       getDenoise(...)
           Returns whether denoise is enabled or disabled for the image style.
       
       getKind(...)
           Get image style kind. Returns lux.IMAGE_STYLE_BASIC or lux.IMAGE_STYLE_PHOTOGRAPHIC
       
       getName(...)
           Get image style name.
       
       getVignette(...)
           Returns whether vignette is enabled or disabled for the image style.
       
       setBloom(...)
           Enable or disable bloom.
           enable = Boolean value for enabling or disabling bloom. *
       
       setChromaticAberration(...)
           Enable or disable chromatic aberration.
           enable = Boolean value for enabling or disabling chromatic aberration. *
       
       setColor(...)
           Enable or disable color for the photographic image style.
           enable = Boolean value for enabling or disabling color. *
       
       setCurve(...)
           Enable or disable curve for the photographic image style.
           enable = Boolean value for enabling or disabling curve. *
       
       setDenoise(...)
           Enable or disable denoise.
           enable = Boolean value for enabling or disabling denoise. *
       
       setKind(...)
           Set image style kind.
           kind = Kind of image style: lux.IMAGE_STYLE_BASIC or lux.IMAGE_STYLE_PHOTOGRAPHIC. *
       
       setVignette(...)
           Enable or disable vignette.
           enable = Boolean value for enabling or disabling vignette. *
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class MaterialGraph(builtins.object)
       MaterialGraph encapsulates a graph of material nodes that constitutes a material in the scene, and enables manipulation of material parameters, adding/removing material nodes, and associating them with input and output edges. Get a material graph by using lux.getMaterialGraph(name).
       
       Methods defined here:
       
       __eq__(self, value, /)
           Return self==value.
       
       __ge__(self, value, /)
           Return self>=value.
       
       __gt__(self, value, /)
           Return self>value.
       
       __hash__(self, /)
           Return hash(self).
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __le__(self, value, /)
           Return self<=value.
       
       __lt__(self, value, /)
           Return self<value.
       
       __ne__(self, value, /)
           Return self!=value.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       executeGeometryNodes(...)
           Executes any pending geometry nodes related to the material of the graph.
       
       getEdgeFromID(...)
           Get edge of material graph specified by edge ID.
           id = Edge ID. *
       
       getMaterialName(...)
           Get graph's material name.
       
       getMaterialNodes(...)
           Get list of material root nodes. For a multi-material, this is the individual sub-material roots. For a regular material, this is a list with a single item that is the same as getRoot().
       
       getNodeFromID(...)
           Get node of material graph specified by node ID.
           id = Node ID. *
       
       getNodes(...)
           Get list of all material nodes of the graph. The edges are considered irrelevant in this function.
       
       getNodesFromType(...)
           Get nodes of material graph specified by node type.
           type = Node type. See `lux.SHADER_TYPE_..` for possibilities. *
       
       getRoot(...)
           Get root node of material graph.
       
       newEdge(...)
           Create new edge between two nodes for a specific parameter in the material graph.
           source = Node ID or lux.ShaderNode instance. *
           target = Node ID or lux.ShaderNode instance. *
           param = Parameter of target to attach source node to. *
       
       newNode(...)
           Create new node in the material graph.
           type = Shader node type to create. See `lux.SHADER_TYPE_..` for possibilities. *
       
       removeEdge(...)
           Remove edge from material graph.
           edge = Edge ID or lux.ShaderEdge instance to remove. *
       
       removeNode(...)
           Remove node from material graph.
           node = Node ID or lux.ShaderNode instance to remove. *
       
       setCurrentSubMaterial(...)
           Set sub-material to specified node.
           node = Node ID or lux.ShaderNode instance to set. *
       
       setMultiMaterial(...)
           Controls multi-material features of material graph. If disabling a multi-material, the current active sub-material will become root of the material and other sub-materials will be removed.
           enable = Enable or disable. *
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class MaterialMetadata(builtins.object)
       The MaterialMetadata exposes the functionality needed to edit CMF meta data for a material.
       Changes made to the metadata are only applied to library.
       Metadata fields of type lux.CMF_KIND_TEXT or lux.CMF_KIND_IMAGE can be edited through this class.
       A metadata field of the image type may be created or updated with a value containing a path-string to an image.
       Alternatively an instance of lux.ThumbnailRenderOptions can be passed as a value when creating/updating an image field.
       This will render a thumbnail for the field.
       Get a MaterialMetadata instance for a specific material by calling:
       lux.findMaterialMetadata(<material_name>).
       Save changes by passing an instance of this class to:
       lux.saveMaterialMetadata(<metadata_instance>)
       
       Methods defined here:
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       createField(...)
           Create a new metadata field for the material.
           name = A string key for the field to be created.
           value = New value for field.
           type = Specifies datatype of the field. Defaults to lux.CMF_KIND_TEXT. Supports lux.CMF_KIND_IMAGE.
       
       deleteField(...)
           Delete metadata field.
           name = String key for the field.
       
       getFieldNames(...)
           List all keys for the metedata Fields of this material.
       
       readField(...)
           Get value of metadata field.
           Does not allow reading fields of type lux.CMF_KIND_IMAGEname = name of field
       
       updateField(...)
           Update value of metadata field.
           name = name of field.
           value = new value for field.
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class MultiMaterial(builtins.object)
       MultiMaterial encapsulates access and modification in a clear and consise way. Create a new multi-material using lux.createMultiMaterial() by giving a name of an existing material to base it off of. Or retrieve a multi-material instance via lux.getMultiMaterial(). A multi-material can be applied to scene nodes by using its name, just like normal materials.
       
       Methods defined here:
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       getActiveMaterial(...)
           Gets the active sub material of the multi-material.
       
       getName(...)
           Gets the name of the multi-material.
       
       getSubMaterials(...)
           Gets the list of sub materials of the multi-material. The order matters.
       
       setActiveMaterial(...)
           Set active sub material of multi-material.
           name = Name of sub material to activate. Must be one of the associated sub materia names! *
       
       setName(...)
           Set multi-material name.
           name = Name of multi-material. *
       
       setSubMaterials(...)
           Sets the list of sub materials of the multi-material. The order matters.
           mats = The list of materials. *
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class RenderOptions(builtins.object)
       RenderOptions encapsulates render options in a clear and concise way. The options can be persisted as a dictionary using getDict() and fed to RenderOptions(dict=your_dict) when employing it.
       
       The rendering mode can be found by the "render_mode" key of the dictionary. It can have three values: lux.RENDER_MODE_ADVANCED, lux.RENDER_MODE_TIME, or lux.RENDER_MODE_SAMPLES.
       
       Get an instance of the current render options using lux.getRenderOptions().
       
       Methods defined here:
       
       __eq__(self, value, /)
           Return self==value.
       
       __ge__(self, value, /)
           Return self>=value.
       
       __gt__(self, value, /)
           Return self>value.
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __le__(self, value, /)
           Return self<=value.
       
       __lt__(self, value, /)
           Return self<value.
       
       __ne__(self, value, /)
           Return self!=value.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       getDict(...)
           Get specified options as a dictionary. This can be useful to persist options and then supply to a lux.RenderOptions() constructor when needed to render something. Be wary of the version specified in the dictionary, key values will be converted to the latest version automatically.
       
       setAddToQueue(...)
           Instead of rendering immediately then it will be added to the internal KeyShot queue, waiting for processing. Note that a copy of the scene will be saved to disk each time. Call lux.processQueue() to process the queue and render what has been added to it.
           add = Whether to add to queue or not. *
       
       setAdvancedRendering(...)
           Render in advanced mode with specified samples.
           samples = The number of samples. *
       
       setAntiAliasing(...)
           Set anti aliasing level.
           level = Value from 1 to 8. *
       
       setBackgroundRendering(...)
           Render in external background process. Note that a background window will open and the call-site will return immediately!
           ext = Whether to render in background or not. *
       
       setCausticsQuality(...)
           Set caustics quality.
           quality = Value from 0 to 10 (0 will disable it). *
       
       setDofQuality(...)
           Set depth-of-field quality.
           quality = Value from 1 to 10. *
       
       setGlobalIllumination(...)
           Set global illumination quality.
           quality = Quality from 0 to 5 (0 will disable it). *
       
       setGlobalIlluminationCache(...)
           Set whether or not to use global illumination cache.
           enable = Use cache. *
       
       setIndirectBounces(...)
           Set the number of indirect bounces.
           bounces = The number of indirect bounces. *
       
       setMaxSamplesRendering(...)
           Render until max samples is reached.
           samples = Maximum samples. *
       
       setMaxTimeRendering(...)
           Render the amount of time specified.
           time = Time in seconds (floating-point number). *
       
       setOutputAlphaChannel(...)
           Set whether to have alpha channel in output image.
           enable = Use alpha channel or not. *
       
       setOutputAmbientOcclusionPass(...)
           Output ambient occlusion pass separate to the result.
           enable = Output ambient occlusion pass. *
       
       setOutputCausticsPass(...)
           Output caustics pass separate to the result.
           enable = Output caustics pass. *
       
       setOutputClownPass(...)
           Output clown pass separate to the result.
           enable = Output clown pass. *
       
       setOutputDepthPass(...)
           Output depth pass separate to the result.
           enable = Output depth pass. *
       
       setOutputDiffusePass(...)
           Output diffuse pass separate to the result.
           enable = Output diffuse pass. *
       
       setOutputDirectLightingPass(...)
           Output direct lighting pass separate to the result.
           enable = Output direct lighting pass. *
       
       setOutputIndirectLightingPass(...)
           Output indirect lighting, or global illumination, pass separate to the result.
           enable = Output indirect lighting pass. *
       
       setOutputLabelsPass(...)
           Output labels pass separate to the result.
           enable = Output labels pass. *
       
       setOutputNormalsPass(...)
           Output normals pass separate to the result.
           enable = Output normals pass. *
       
       setOutputRawPass(...)
           Output RAW pass separate to the result.
           enable = Output RAW pass. *
       
       setOutputReflectionPass(...)
           Output reflection pass separate to the result.
           enable = Output reflection pass. *
       
       setOutputRefractionPass(...)
           Output refraction pass separate to the result.
           enable = Output refraction pass. *
       
       setOutputRenderLayers(...)
           Output render layers separate to the result
           enable = Output render layers. *
       
       setOutputShadowPass(...)
           Output shadow pass separate to the result.
           enable = Output shadow pass. *
       
       setPixelBlur(...)
           Set pixel blur.
           blur = Value from 1 to 3. *
       
       setRayBounces(...)
           Set the number of ray bounces.
           bounces = The number of ray bounces. *
       
       setRegion(...)
           Set render region to get subset of image.
           region = Tuple/list of (start x-axis, start y-axis, end x-axis, end y-axis). Use None to unset a region. *
       
       setSendToNetwork(...)
           Instead of rendering locally it can be done using KeyShot Network Rendering.
           send = Whether to send to network or not. *
       
       setShadowQuality(...)
           Set shadow quality.
           quality = Value from 1 to 10. *
       
       setSharpShadows(...)
           Set whether to have sharp shadows or not.
           enable = Output sharp shadows. *
       
       setSharperTextureFiltering(...)
           Set whether or not to preserve detail in textures when viewed at grazing angles.
           enable = Output sharper texture filtering. *
       
       setThreads(...)
           Set the number of rendering threads. Zero threads means one thread per core.
           threads = The number of threads. *
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
       
       ----------------------------------------------------------------------
       Data and other attributes defined here:
       
       __hash__ = None
    
    class SceneNode(builtins.object)
       SceneNode encapsulates a node in the scene tree and enables for manipulation, such as hiding/showing, locking/unlocking, setting materials etc., and traversal of the tree. It provides a means for searching and accessing groups, objects and animations for global and local operations. Get an instance of the root of the scene tree using lux.getSceneTree().
       
       Methods defined here:
       
       __eq__(self, value, /)
           Return self==value.
       
       __ge__(self, value, /)
           Return self>=value.
       
       __gt__(self, value, /)
           Return self>value.
       
       __hash__(self, /)
           Return hash(self).
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __le__(self, value, /)
           Return self<=value.
       
       __lt__(self, value, /)
           Return self<value.
       
       __ne__(self, value, /)
           Return self!=value.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       applyTransform(...)
           Apply a transformation (luxmath.Matrix) to the node and its children.
           For example, to scale the node to 1/10 of the size:
             T = luxmath.Matrix().makeIdentity().scale(0.1)
             node.applyTransform(T)
           Where 'node' is your lux.SceneNode.
           Or move an object to absolute position (1, 2, 3):
             T = luxmath.Matrix().makeIdentity().translate(luxmath.Vector((1, 2, 3)))
             node.applyTransform(T, absolute = True)
           
           trans = The transformation (luxmath.Matrix) to apply. *
           absolute = Whether to make an absolute transformation instead of a relative one. Must be an object node for absolute transform. (default = False)
       
       centerAndFit(...)
           Centers and fits the node.
       
       delete(...)
           Delete node.
       
       deselect(...)
           Visually deselects node in the scene.
       
       dump(...)
           Returns a string representation of the node and its children.
       
       duplicate(...)
           Duplicate current node and subtree.
           amount = The amount of duplicates to create (default = 1).
           linkMats = Whether to link materials or not (default = false).
       
       find(...)
           Find nodes in the subtree of this node by searching part names and material names. If no names or materials are given then it will find everything.
           name = Part name to search for (string/tuple/list). 
           mat = Material name to search for (string/tuple/list). 
           all = Match all part names or all material names (default = false).
           types = Filter results to match types (int/tuple/list) which can be the following the values: lux.NODE_TYPE_GROUP, lux.NODE_TYPE_OBJECT, lux.NODE_TYPE_ANIMATION, lux.NODE_TYPE_MODEL_SET, lux.NODE_TYPE_MODEL and lux.NODE_TYPE_CAMERA default = all types). 
           depth = The amount of levels to go down the tree. A value of 1 means to only match the direct children of this node etc. (default = -1 = all)
           deleted = Whether or not to include deleted nodes. (default = False)
       
       getBoundingBox(...)
           Get bounding box of node as a tuple of two vectors: min and max.
           world = Whether to be in world space or not (default = false).
       
       getCenter(...)
           Get the center of this node.
           world = Whether to be in world space or not (default = false).
       
       getChildren(...)
           Get children of group.
       
       getDeleted(...)
           Get deleted nodes of a group (recursive).
       
       getHidden(...)
           Get hidden nodes of a group (recursive).
       
       getID(...)
           Get node ID.
       
       getKind(...)
           Get node kind. Can be one of the following values: lux.NODE_TYPE_GROUP, lux.NODE_TYPE_OBJECT, lux.NODE_TYPE_ANIMATION, lux.NODE_TYPE_MODEL_SET, lux.NODE_TYPE_MODEL or lux.NODE_TYPE_CAMERA.
       
       getLocked(...)
           Get locked nodes of a group (recursive).
       
       getMaterial(...)
           Get material of a node.
       
       getName(...)
           Get node name.
       
       getParent(...)
           Get parent node of this node.
       
       getPath(...)
           Get path from root to this node as a tuple of lux.SceneNode objects.
           text = Whether to return the names instead of lux.SceneNode objects (default = false).
       
       getRenderLayer(...)
           Get render layer for associated node, if any.
       
       getSelected(...)
           Get selected nodes of a group (recursive).
       
       getTransform(...)
           Get the transformation matrix of this node.
           world = Whether to be in world space or not (default = false).
       
       hide(...)
           Hide node.
       
       isAnimation(...)
           Check if node is an animation.
       
       isCamera(...)
           Check if node is a camera.
       
       isDeleted(...)
           Check if node is deleted.
       
       isDescendantOf(...)
           Checks if this node is a descendant of the input group node.
           group = Group node to check sub-tree of. *
       
       isGroup(...)
           Check if node is a group.
       
       isHidden(...)
           Check if node is hidden.
       
       isLocked(...)
           Check if node is locked.
       
       isModel(...)
           Check if node is a model (direct child of a model set).
       
       isModelSet(...)
           Check if node is a model set.
       
       isObject(...)
           Check if node is an object.
       
       isSelected(...)
           Check if node is selected in the scene.
       
       lock(...)
           Lock node.
       
       moveToGroup(...)
           Move this node to another group node. Note: This changes the scene tree.
           group = Group node to move this node to. *
       
       select(...)
           Visually selects node in the scene.
       
       setMaterial(...)
           Set material of a node. If applying to a group then it will apply to all sub nodes.
           mat = The name of the material or multi-material to apply. It can also be an instance of lux.MultiMaterial. *
           link = Whether to link to the material or create a duplicate. (default = False)
       
       setName(...)
           Set name of node.
           name = New name of node. *
       
       setRenderLayer(...)
           Associate node with render layer, creating it if name is non-existent. Current render layer will be unset if name is unspecified or empty.
           name = Render layer name. (See available ones with lux.getRenderLayers())
       
       show(...)
           Show node if hidden.
       
       snapToGround(...)
           Snaps node to ground plane.
       
       undelete(...)
           Undelete node.
       
       unlock(...)
           Unlock node.
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class ShaderEdge(builtins.object)
       ShaderEdge encapsulates a shader edge from a source shader node to a target shader node as part of a material graph. Get a shader edge via a shader node from a material graph instance.
       
       Methods defined here:
       
       __eq__(self, value, /)
           Return self==value.
       
       __ge__(self, value, /)
           Return self>=value.
       
       __gt__(self, value, /)
           Return self>value.
       
       __hash__(self, /)
           Return hash(self).
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __le__(self, value, /)
           Return self<=value.
       
       __lt__(self, value, /)
           Return self<value.
       
       __ne__(self, value, /)
           Return self!=value.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       getID(...)
           Get shader edge's ID.
       
       getSourceNode(...)
           Get source node of shader edge.
       
       getTargetNode(...)
           Get target node of shader edge.
       
       isEnabled(...)
           Checks if shader edge is enabled.
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class ShaderNode(builtins.object)
       ShaderNode encapsulates a shader node as part of a material graph, and enables manipulation of material parameters. Get a shader node via a material graph instance.
       
       Methods defined here:
       
       __eq__(self, value, /)
           Return self==value.
       
       __ge__(self, value, /)
           Return self>=value.
       
       __gt__(self, value, /)
           Return self>value.
       
       __hash__(self, /)
           Return hash(self).
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __le__(self, value, /)
           Return self<=value.
       
       __lt__(self, value, /)
           Return self<value.
       
       __ne__(self, value, /)
           Return self!=value.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       getID(...)
           Get shader node's ID.
       
       getInputEdge(...)
           Get input edge with specified parameter name.
           parameter = Name of parameter. *
       
       getInputEdges(...)
           Get all input edges to this shader node.
       
       getName(...)
           Get shader node's name.
       
       getOutputEdges(...)
           Get all output edges from this shader node.
       
       getParameter(...)
           Get parameter with specific name of this shader node.
           name = Name of parameter. *
       
       getParameters(...)
           Get all parameters of this shader node.
       
       getType(...)
           Get shader node's type consisting of a shader type name and human-friendly name.
       
       setName(...)
           Set shader node's name.
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class ShaderParameter(builtins.object)
       ShaderParameter encapsulates a parameter of a shader node as part of a material graph. Get a shader parameter via a shader node instance.
       
       Methods defined here:
       
       __hash__(self, /)
           Return hash(self).
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       getColor(...)
           Get concrete value of shader parameter. Cannot be called on pure parameters.
       
       getDisplayName(...)
           Get display name of shader parameter.
       
       getName(...)
           Get name of shader parameter.
       
       getType(...)
           Get type of shader parameter. All supported types are found as `lux.PARAMETER_TYPE_...`.
       
       getValue(...)
           Get concrete value of shader parameter. Cannot be called on pure parameters.
       
       isPure(...)
           Checks if shader parameter is pure, i.e. has no concrete value. Pure parameters cannot get/set concrete values on them!
       
       setValue(...)
           Set concrete value of shader parameter. Cannot be called on pure parameters.
           value = The supported input types depend on the shader parameter type. *
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class Studio(builtins.object)
       Studio encapsulates studio settings in a clear and consise way.
       
       Methods defined here:
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       __repr__(self, /)
           Return repr(self).
       
       __str__(self, /)
           Return str(self).
       
       enableMultiMaterials(...)
           Enable or disable multi materials on the studio.
           enable = Boolean value for enabling or disabling multi materials. (default = True)
       
       getCamera(...)
           Get studio camera (name)
       
       getEnvironment(...)
           Set studio environment in the form of its name.
       
       getImageStyle(...)
           Set studio image style in the form of its name.
       
       getModelSets(...)
           Get studio model sets. It returns a list of model set names.
       
       getMultiMaterials(...)
           Get studio multi materials. Returns a list of (MaterialName, ActiveSubMaterialName) tuples for each multi material in the studio.
       
       getName(...)
           Get studio name.
       
       isMultiMaterialsEnabled(...)
           Returns whether multi materials are enabled for the studio.
       
       setCamera(...)
           Set studio camera.
           name = The camera in the form of its name or `None` to disable. *
       
       setEnvironment(...)
           Set studio environment.
           name = The environment in form of its name or `None` to disable. *
       
       setImageStyle(...)
           Set studio Image Style.
           name = The image style in form of its name or `None` to disable. *
       
       setModelSets(...)
           Set studio modelsets.
           names = A List of model sets (specified by a list of model set names) or `None` to disable. *
       
       updateMultiMaterial(...)
           Make the submaterial active for the given multimaterial in the studio.
           multimaterial = The name of a multimaterial in the studio *
           submaterial = The name of the submaterial to activate *
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
    
    class ThumbnailRenderOptions(builtins.object)
       Encapsulates settings for rendering material thumbnails.
       Can be passed as value parameter for .update() or .create() on a metadata instance retrieved with lux.findMaterialMetadata()
       Constructor expects a model-ID as a parameter. A model id dictates which model is used for the render.
       Accepted model-IDs are:
       lux.MODEL_ID_MATERIAL_DISC_25_MM
       lux.MODEL_ID_MATERIAL_DISC_100_MM
       lux.MODEL_ID_MATERIAL_DISC_1_M
       lux.MODEL_ID_MATERIAL_DISC_TOON_100_MM
       lux.MODEL_ID_CLOTH_DRAPE
       lux.MODEL_ID_LIQUID_GLASS
       lux.MODEL_ID_CRYSTAL
       lux.MODEL_ID_SPHERE_CUTAWAY_100_MM
       lux.MODEL_ID_LUXION_SPHERE
       If no model ID is passed as a constructor parameter, a defualt model will be used for the thumbnail render.
       
       Methods defined here:
       
       __init__(self, /, *args, **kwargs)
           Initialize self.  See help(type(self)) for accurate signature.
       
       ----------------------------------------------------------------------
       Static methods defined here:
       
       __new__(*args, **kwargs) from builtins.type
           Create and return a new object.  See help(type) for accurate signature.
FUNCTIONS
    applyMaterialMapping(...)
        Applies a material mapping.
        dict = Dictionary of object IDs to material names. *
        link = Whether to link to the material or create a duplicate. (default = False)
    
    clearGeometry(...)
        Clears all geometry in the scene.
        ask = Whether to ask to clear or not (default = false, only in GUI mode).
    
    createColorway(...)
        Create a new colorway in the scene
        name = Name of color. Must be unique!*
    
    createMultiMaterial(...)
        Create a multi-material based on an existing material.
        name = Name of new multi-material. *
        mat = Name of existing material to clone from. Can be a string or list of strings (first item of the list will be used to clone from). *
    
    createSceneColor(...)
        Create a new color in the scene
        name = Name of color. Must be unique!
        multi = Set to create multi color*
    
    createSceneMaterial(...)
        Creates a new scene material (diffuse).
        name = Name of material to create. *
    
    deleteColorway(...)
        Delete a colorway in the scene
        colorway = Colorway to delete. Either object or name. *
    
    deleteMaterial(...)
        Deletes material from KeyShot context. Note: It is required that resource libraries are loaded once per session - the operation blocks while loading.
        name = Name of material to delete. *
    
    dumpTree(...)
        Dumps the scene tree as a JSON string.
    
    enablePerformanceMode(...)
        Enable or disable performance rendering mode.
        enable = Whether to enable or not. (default = true)
    
    encodeVideo(...)
        Encodes a video from frames of a folder.
        folder = Folder to encode video frames from. *
        frameFiles = Name of the frame files. The extension dictates the image format (can be jpg/jpeg, png, exr, or tif/tiff). *
        videoName = Name of the video file, if any. The extension dictates the video format (can be mp4, mov, avi, or flv). *
        fps = Frames per second. Relates to the number of frames available! *
        firstFrame = Frame to start encoding from (defaults to scene settings).
        lastFrame = Frame to end encoding at (defaults to scene settings).
        keepFrames = Whether to keep the frames after encoding (default = true)
        opts = Options specified as a lux.RenderOptions object (see lux.getRenderOptions()).
    
    exportFile(...)
        Export scene to a file of specified format.
        path = Path to export file to. *
        format = Export format can be one of the following values: lux.EXPORT_OBJ, lux.EXPORT_FBX, lux.EXPORT_GLTF (will be saved as GLB if the file extension is '.glb'), lux.EXPORT_STL, lux.EXPORT_3MF, lux.EXPORT_USD. *
        mode = Optional texture mode dictionary to provide additional information. The dictionary has the following form:
          {"mode": mode}
        where mode can be one of the following values: lux.EXPORT_SINGLE_COLOR (STL), lux.EXPORT_VERTEX_COLOR (STL), lux.EXPORT_BAKING (GLTF, THREEMF, USD). Some modes can take additional options:
          {"mode": lux.EXPORT_VERTEX_COLOR,
           "sub_div": sub_div,
           "stop_criteria": stop_criteria,
           "poly_count": poly_count,
           "edge_length": edge_length}
        where sub_div can be either lux.EXPORT_SUB_DIV_NORMAL or lux.EXPORT_SUB_DIV_ADAPTIVE, and stop_criteria can be lux.EXPORT_SUB_DIV_POLYCOUNT or lux.EXPORT_SUB_DIV_EDGE_LENGTH.
          {"mode": lux.EXPORT_BAKING,
           "dpi": dpi,
           "num_samples": number_of_samples,
           "occlusion": include_ambient_occlusion_boolean,
           "draco_compression": Compress using Draco (only GLTF/B),
           "preferred_output": Prefer textures or geometry shaders when parts have both
           "keep_uvs": Use original UVs if possible}
        where preferred_output can be either lux.EXPORT_OUTPUT_TEXTURES or lux.EXPORT_OUTPUT_GEOMETRY_SHADERS.
    
    findMaterialMetadata(...)
        Retrieve an object with the ability to access/modify metadata for a specific material in the material library.
        name = Name of material. *
    
    getActiveConfiguration(...)
        Returns a dict of the current active configuration.
    
    getActiveEnvironment(...)
        Get active environment instance for manipulating and retrieving information.
    
    getActiveImageStyle(...)
        Get active image style instance for manipulating and retrieving information.
    
    getActiveStudio(...)
        Get active studio of the scene. Yields name or instance.
        instance = Return lux.Studio instance instead of name. (default = False)
    
    getAnimationFrame(...)
        Returns the current animation frame.
    
    getAnimationInfo(...)
        Returns information about the animation; the duration in seconds, and the amount of frames.
    
    getAnimationTime(...)
        Returns the current animation time in seconds.
    
    getBrowserDialog(...)
        Show browser dialog. Specify either URL or HTML contents.
        url = URL to load inside browser dialog (use 'file:///' to load local files).
        html = HTML contents to load inside browser dialog.
        result = Lambda expression or function to evaluate when "lux.yieldResult(..)" is called in JavaScript on the page inside the browser dialog. It will be invoked with the result dictionary (JS Object) as parameter. Note that the earliest time to use the function in JS is when the page is loaded, i.e. the 'load' event, and up to 500ms later. The functionality is automatically loaded onto the page. (default = None)
        init = Dictionary of data to initialize the "lux.initData" with in JavaScript of the browser dialog. (default = None)
    
    getCamera(...)
        Retrieves the currently active camera of the scene.
    
    getCameraDirection(...)
        Gets the direction of the active camera of the scene.
    
    getCameraDistance(...)
        Get distance from active camera to pivot/look-at point.
    
    getCameraFieldOfView(...)
        Gets the field of view of the active camera of the scene.
    
    getCameraFocalLength(...)
        Gets the focal length of the active camera of the scene.
    
    getCameraLens(...)
        Get lens information of active camera of the scene as a dictionary.
        The "lens" value will be one of lux.CAMERA_TYPE_ORTHOGRAPHIC, lux.CAMERA_TYPE_PERSPECTIVE, 
        lux.CAMERA_TYPE_SHIFT, lux.CAMERA_TYPE_PANORAMA, or lux.CAMERA_TYPE_PERSPECTIVE_STEREO.
        The values "fov" and "perspective" are only included for perspective and shift cameras.
        The values "vertical_shift" and "horizontal_shift" are only included for shift cameras.
        The "mode" value is only included for panoramic cameras and will be either 
        lux.PANORAMA_TYPE_SPHERICAL or lux.PANORAMA_TYPE_CUBEMAP.
    
    getCameraLookAt(...)
        Gets the lool-at point of the active camera of the scene.
    
    getCameraPosition(...)
        Gets the position of the active camera of the scene.
    
    getCameraUp(...)
        Gets the up vector of the active camera of the scene.
    
    getCameras(...)
        Retrieves the cameras of the scene.
    
    getColorway(...)
        Get lux.Colorway object representing the colorway denoted by the colorway name.
        colorway = Colorway to access. Either object or name. *
    
    getColorways(...)
        Gets colorways of the scene.
    
    getEnvironments(...)
        Get list of environents of the scene.
    
    getExternalFiles(...)
        Returns a list of all external files needed by the current scene.
    
    getImageStyles(...)
        Get list of image styles of the scene.
    
    getImportOptions(...)
        Returns import options in a dictionary:
         accurate_tessellation: Use alternative tessellation method when available.
         adjust_camera_look_at: Adjust active camera to look at the imported geometry.
         adjust_environment: Adjust environment sphere to fit the imported geometry.
         camera_import: Import cameras if able.
         center_geometry: Center newly added geometry in the scene.
         snap_to_ground: Snap newly imported geometry to the ground plane.
         compute_normals: Compute normals during import, if the format allows.
         geometry_units: The unit of the imported scene, if not automatically detected. Supply as conversion factor from meters, e.g. cm = 100, feet = 3.2808399, etc.
         include_nurbs: Include NURBS data.
         import_type: How to import to scene. Add to scene = 0, Update active geometry = 1, Clear and  import to new scene = 2.
         merge_groups: Apply some post import merging to identically named groups.
         merge_objects: Apply some post import merging to identically named objects.
         retain_materials: Apply material changes to the active model to the imported model.
         separate_materials: Ensure that materials are not linked across parts.
         separate_parts: Prevent objects from being merged during import. Certain formats only.
         tessellation_quality: Tessellation quality from 0.0 to 1.0. Higher values should yield more triangles.
         up_vector: Up vector of the source program. x = 0, y = 1, z = 2, -x = 3, -y = 4, -z = 5
         frame: Import a specific animation frame, if able.
         mayaForceVersion: Maya file import depends on a local Maya installation. This option forces the importer to use a specific version. Should be a string representing the year release, e.g. "2013".
         group_by: For importers with multiple grouping options. Group by Layer = 0, Group by Shader = 1, Group by Object = 2.
         model_set_import_to: Which model set to import to. All = 0, Active = 1, Selected = 2, New = 3
        selected_model_set_ids = List of ids of model sets to import to when model_set_import == 2. Get model set id with GetId() on a lux.SceneNode.
        ext = File extension to get specific options.
        getDefaults = Whether to get KeyShot defaults or user settings from a previous import (default = false).
        inclusion_options = A bitwise collection of flags determining which features to import. 0 = Nothing, 1 = Geometry, 2 = Cameras, 4 = Environments, 8 = Image Styles, 16 = Studios. To include geometry and cameras set to 3 (since 1 + 2 = 3). Set to 31 for all features.
        instanceNames = Use instance-level naming for NX and Catia based formats.
    
    getInputDialog(...)
        Show dialog according to the arguments provided and return the results. It returns None if cancelled.
        
        For example, to show a dialog asking a string, an integer between 10 and 50 that has default value 42, and an item of [1, 2, 3]:
            values = [("string", lux.DIALOG_TEXT, "Input string:", "hello"),
                      ("int", lux.DIALOG_INTEGER, "Input int:", 42, (10, 50)),
                      (lux.DIALOG_LABEL, "Freestanding label text."),
                      ("item", lux.DIALOG_ITEM, "Select item:", 2, [1, 2, 3])]
            opts = lux.getInputDialog(title = "This is the title", values = values)
        The returned options, with default values, would be:
            {"string": "hello", "int": 42, "item": [1, "2"]}
        
        Another trick is using a lambda when clicking "Apply" so the dialog does not need to close every time, and it gets a more interactive feel.
            values = [("string", lux.DIALOG_TEXT, "Text:", "test")]
            lux.getInputDialog(title = "Testing Apply", values = values,
                               apply = lambda res: print(res))
        In this case it means that whenever "Apply" is clicked the result will be printed to console.
        
        title = Title of the dialog. *
        
        desc = Description of dialog. (default = None) 
        
        values = The values of the dialog to build and show. It expects a list of tuples, one tuple for each control. The tuple must contain four or five values depending on the type: key, type, label, and default value, with the additional constraints value in some cases. The key is a string, the label is a string, the type can be one of the following values: lux.DIALOG_TEXT, lux.DIALOG_INTEGER, lux.DIALOG_DOUBLE, lux.DIALOG_ITEM, lux.DIALOG_CHECK, lux.DIALOG_FILE, lux.DIALOG_FOLDER, or lux.DIALOG_LABEL. If the type is lux.DIALOG_INTEGER or lux.DIALOG_DOUBLE then the extra constraints value must be present in the tuple, which is a tuple of minimum and maximum value, and if the type is lux.DIALOG_ITEM then the extra argument must be a list of items to select from. As a special case, if the type is lux.DIALOG_LABEL then the tuple size must be two and the second value must be a string (if the string contains only dashes then it becomes a horizontal divider). * 
        
        id = Special ID to enable persisting values and when reopening. If given then clicking OK will remember the values so that if the ID is used again then the values will be the default values. Make sure that the ID is unique enough so other scripts won't use it by accident. (default = None)
        
        apply = Lambda expression or function to evaluate when "Apply" is clicked in the dialog. It will be invoked with the result dictionary as parameter. The dialog will not close when "Apply" is clicked. (default = None)
    
    getInputDouble(...)
        Show dialog to input a double.
        title = Title of the dialog (default = "Enter double").
        label = Label of the dialog (default = "Enter double:").
        value = Initial value (default = 0).
        min = Minimum value (default = -2147483647).
        max = Maximum value (default = 2147483647).
        decimal = Maximum number of decimal places (default = 1).
    
    getInputFile(...)
        Show dialog to select file(s) from the file system.
        multiple = If multiple files can be selected (default = false).
        title = Title of the dialog (default = "Select file(s)").
        folder = The folder to show initially (default = home folder).
        filter = Filter of files to allow selection from (default = none). An example could be "*.obj *.bip" for all OBJs and BIPs.
    
    getInputFolder(...)
        Show dialog to select a folder from the file system.
        title = Title of the dialog (default = "Select folder").
        folder = The folder to show initially (default = home folder).
    
    getInputInt(...)
        Show dialog to input an integer.
        title = Title of the dialog (default = "Enter integer").
        label = Label of the dialog (default = "Enter integer:").
        value = Initial value (default = 0).
        min = Minimum value (default = -2147483647).
        max = Maximum value (default = 2147483647).
        step = Stepping amount (default = 1).
    
    getInputItem(...)
        Show dialog to select an item from a list/tuple of items.
        items = List/tuple of items to choose from. *
        title = Title of the dialog (default = "Select item").
        label = Label of the dialog (default = "Select item:").
        current = Index of initial item (default = 0).
        editable = If editable or not (default = true).
    
    getInputText(...)
        Show dialog to input a string.
        title = Title of the dialog (default = "Enter text").
        label = Label of the dialog (default = "Enter text:").
        value = Initial value (default = empty string).
    
    getKeepAspectRatio(...)
        Yield whether aspect ratio is being kept.
    
    getKeyShotDisplayVersion(...)
        Returns the KeyShot display version as a (major, minor) tuple.
    
    getKeyShotFolder(...)
        Returns the path to the specified KeyShot folder.
        type = Type of folder to retrieve can be lux.FOLDER_ANIMATIONS, lux.FOLDER_BACKPLATES, lux.FOLDER_COLORS, lux.FOLDER_CONFIG_ROOT, lux.FOLDER_DOWNLOADS, lux.FOLDER_ENVIRONMENTS, lux.FOLDER_EXTERNAL_PLUGIN, lux.FOLDER_FAVORITES, lux.FOLDER_MATERIALS, lux.FOLDER_MATERIAL_TEMPLATES, lux.FOLDER_MODELS, lux.FOLDER_RESOURCE_ROOT, lux.FOLDER_SCENES, lux.FOLDER_SCREENSHOTS, lux.FOLDER_SCRIPTS, or lux.FOLDER_TEXTURES. *
    
    getKeyShotVersion(...)
        Returns the KeyShot version as a (major, minor, patch, build) tuple.
    
    getLibraryBackplates(...)
        Gets all backplates of the library. Note: It is required that resource libraries are loaded once per session - the operation blocks while loading.
        filter = Filter by relative path in library, e.g. 'Backplates/Outdoor'.
    
    getLibraryColors(...)
        Gets all colors of the library. Note: It is required that resource libraries are loaded once per session - the operation blocks while loading.
        filter = Filter by relative path or name, e.g. 'RAL Colours'.
    
    getLibraryEnvironments(...)
        Gets all environments of the library. Note: It is required that resource libraries are loaded once per session - the operation blocks while loading.
        filter = Filter by relative path in library, e.g. 'Environments/Studio/Basic'.
    
    getLibraryMaterials(...)
        Gets all materials of the library. Note: It is required that resource libraries are loaded once per session - the operation blocks while loading.
        filter = Filter by relative path in library, e.g. 'Materials/Metal/Titanium'.
    
    getLibraryTextures(...)
        Gets all textures of the library. Note: It is required that resource libraries are loaded once per session - the operation blocks while loading.
        filter = Filter by relative path in library, e.g. 'Textures/Wood'.
    
    getLightingPreset(...)
        Get currently used lighting preset.
    
    getLightingPresets(...)
        Get list of lighting presets, both default and custom ones.
    
    getLockResolution(...)
        Yield whether resolution is locked.
    
    getMaterialGraph(...)
        Get lux.MaterialGraph object representing the material graph denoted by the material name.
        name = Material name to access. *
    
    getMaterialMapping(...)
        Gets material mapping: object ID -> material name.
    
    getMaterialTemplates(...)
        Gets material template names.
    
    getMessageBox(...)
        Show message box.
        msg = Descriptive text of message box. *
        title = Title of message box. Note that it doesn't show on macOS. (default is empty).
        type = Type of message box: lux.MESSAGE_BOX_INFO, lux.MESSAGE_BOX_WARNING, lux.MESSAGE_BOX_CRITICAL (default = lux.MESSAGE_BOX_INFO).
    
    getMetaData(...)
        Get meta data of scene.
        format = Format of meta data can be lux.META_DATA_SIMPLE (simple format .meta) or lux.META_DATA_XMP (XML). (default = XMP)
    
    getModelSets(...)
        Returns the list of active model sets.
    
    getMultiMaterial(...)
        Get multi-material instanced from material name.
        name = Name of multi-material. *
    
    getOS(...)
        Returns the OS version string.
    
    getObjectMaterial(...)
        Gets the material applied to the object(s).
        obj = Object ID or list of IDs. *
    
    getObjects(...)
        Gets the object IDs of the scene.
    
    getRenderEngine(...)
        Get render engine currently in use.
    
    getRenderLayers(...)
        Returns a list of render layers in the current scene.
    
    getRenderOptions(...)
        Returns render options as a lux.RenderOptions object. If defaults is set then it will return the internal defaults, otherwise it's the values as they appear in the render dialog.
        defaults = Return defaults or not (default = false).
    
    getSceneColor(...)
        Get lux.ColorParameter object representing the color denoted by the color name.
        name = Color name to access.
        multi = get color or multicolor*
    
    getSceneColors(...)
        Gets currently used colors and multi colors of the scene.
    
    getSceneInfo(...)
        Returns information about the scene in a dict: name, file name, unit/meter scale and number of triangles, objects, nurbs, curves, scene width/height, and rendering width/height.
    
    getSceneMaterials(...)
        Gets currently used materials of the scene.
    
    getSceneTree(...)
        Get lux.SceneNode object representing the root of the scene tree.
    
    getSphericalCamera(...)
        Get spherical information in degrees of active camera as a list: azimuth, inclination, and
        twist.
    
    getStudio(...)
        Returns a studio object that can be used to modified the studio based on a studio name.
        name = Name of studio. *
    
    getStudios(...)
        Get studios of the scene. Yields names or instances.
        instances = Return lux.Studio instances instead of names. (default = False)
    
    getSystemInfo(...)
        Returns information about the system as a dictionary.
    
    hasContents(...)
        Determine if there is any content in the scene.
    
    importFile(...)
        Imports a file.
        path = File path to import. *
        showOpts = Show options dialog (default = false, only in GUI mode).
        dontAsk = Whether or not to suppress blocking dialogs while script is running, e.g. save scene (default = true, only in GUI mode).
        opts = Options specified as a dictionary (see lux.getImportOptions()).
    
    importMaterials(...)
        Imports materials from a MTL or KMP file into material library. Note: It is required that resource libraries are loaded once per session - the operation blocks while loading.
        file = MTL/KMP file path to import materials from. *
        folder = The existing sub material library folder to add the materials to, i.e. 'Glass/Basic' (default = '.', which is the root materials folder).
    
    isCameraUnsaved(...)
        Checks if current camera has unsaved changes.
    
    isHeadless(...)
        Returns whether KeyShot is running in headless or GUI mode.
    
    isPaused(...)
        Checks if renderer is paused.
    
    isPerformanceModeEnabled(...)
        Checks if performance rendering mode is enabled.
    
    isSceneChanged(...)
        Checks if scene has been changed.
    
    isUndoEnabled(...)
        Check whether undo/redo stack is enabled.
    
    loadMaterials(...)
        Loads materials from MTL file as in-project materials, i.e. they will not show up in the material library visually.
        file = MTL File path to load materials from. *
    
    newCamera(...)
        Creates a new camera and makes it active. If not creating unique name and the name exists then it returns false.
        name = The name of the camera to create. *
        unique = Whether to create a unique name using numbers at the end (default = false)
    
    newEnvironment(...)
        Create a new environment.
        name = The name of the new environment to create. *
        activate = Whether or not to activate the new environment. (default = True)
        clone = Whether or not to clone the current environment. (default = True)
    
    newImageStyle(...)
        Create a new image style.
        name = The name of the new image style to create. *
        kind = Kind of image style: lux.IMAGE_STYLE_BASIC or lux.IMAGE_STYLE_PHOTOGRAPHIC. (default = lux.IMAGE_STYLE_BASIC)
        activate = Whether or not to activate the new image style. (default = True)
    
    newModelSet(...)
        Create a new model set.
        name = The name of the new model set to create. *
    
    newScene(...)
        Clears the scene.
        dontAsk = Whether or not to suppress blocking dialogs while script is running, e.g. save scene (default = true, only in GUI mode).
    
    newStudio(...)
        Create a new studio.
        name = Name of studio. *
    
    openFile(...)
        Opens or imports a file. KSP files will be imported into the KeyShot resources folder.
        path = File path to open. *
        dontAsk = Whether or not to suppress blocking dialogs while script is running, e.g. save scene (default = true).
    
    openPackage(...)
        Opens a package (KSP).
        path = KSP file path to open. *
        resources = Path to extract the resources to. (default = KeyShot resource folder).
        NOTE: folder removal is required if manually specifying resources folder.
        dontAsk = Whether or not to suppress blocking dialogs while script is running, e.g. save scene (default = true).
    
    pause(...)
        Pauses renderer.
    
    prettyPrint(...)
        Returns pretty representation of input object.
    
    processQueue(...)
        Process render queue.
    
    removeCamera(...)
        Removes a camera.
        name = The name of the camera to remove. *
    
    removeEnvironment(...)
        Removes an environment.
        name = The name of the environment to remove. *
    
    removeImageStyle(...)
        Removes an image style.
        name = The name of the image style to remove. *
    
    removeModelSet(...)
        Remove a model set. If current model set is to be removed then the default model set is chosen.
        name = The name of the new model set to remove. *
    
    removeStudio(...)
        Removes a studio.
        name = Name of studio. *
    
    renderAnimation(...)
        Renders frames of the scene to a folder and/or video file.
        folder = Folder to render frames to. *
        frameFiles = Name of the frame files. The extension dictates the image format (can be jpg/jpeg, png, exr, tif/tiff or psd). (default = "frame.%d.jpg")
        keepFrames = Whether to keep the frames after rendering (default = true).
        width = Resolution width in pixels of the frames (default = scene width).
        height = Resolution height in pixels of the frames (default = scene height).
        fps = Frames per second (default = 12).
        videoName = Name of the video file, if any. The extension dictates the video format (can be mp4, mov, avi, or flv). (default = none)
        opts = Options specified as a lux.RenderOptions object (see lux.getRenderOptions()).
        format = Image format. Can be one of the following values: lux.RENDER_OUTPUT_JPEG, lux.RENDER_OUTPUT_PNG, lux.RENDER_OUTPUT_EXR, lux.RENDER_OUTPUT_TIFF8, lux.RENDER_OUTPUT_TIFF32, lux.RENDER_OUTPUT_PSD8, lux.RENDER_OUTPUT_PSD16, lux.RENDER_OUTPUT_PSD32 (requires file extension to match).
    
    renderCMF(...)
        Renders the scene to an image file.
        folder = Folder path to render to.*
        imageName = Filename of the cmf output. The extension dictates the image format(can be jpg/jpeg, png). 
        calloutsOnly = Only list materials with active callouts
        pagetemplate = Uses a page template - (default = portrait)
        width = Resolution width in pixels of the output image (default = scene width).
        height = Resolution height in pixels of the output image (default = scene height).
        opts = Options specified as a lux.RenderOptions object (see lux.getRenderOptions()).
    
    renderConfiguration(...)
        Renders a configuration of the scene.
        name = Name of configuration. It must contain an image extension: jpg, jpeg, or png. For images mode the name must also contain '%d'. *
        folder = Folder to render files to. *
        web = Whether or not to render web files (default = False).
        modelVariations = Enable model variations for images mode (default = False).
        materialVariations = Enable material variations for images mode (default = False).
        studioVariations = Enable studio variations for images mode (default = False).
        opts = Options specified as a lux.RenderOptions object (see lux.getRenderOptions()).
    
    renderFrames(...)
        Renders frames of the scene to a folder.
        folder = Folder to render frames to. *
        frameFiles = Name of the frame files. The extension dictates the image format (can be jpg/jpeg, png, exr, tif/tiff or psd). (default = "frame.%d.jpg")
        width = Resolution width in pixels of the frames (default = scene width).
        height = Resolution height in pixels of the frames (default = scene height).
        fps = Frames per second (default = 12).
        opts = Options specified as a lux.RenderOptions object (see lux.getRenderOptions()).
        format = Image format. Can be one of the following values: lux.RENDER_OUTPUT_JPEG, lux.RENDER_OUTPUT_PNG, lux.RENDER_OUTPUT_EXR, lux.RENDER_OUTPUT_TIFF8, lux.RENDER_OUTPUT_TIFF32, lux.RENDER_OUTPUT_PSD8, lux.RENDER_OUTPUT_PSD16, lux.RENDER_OUTPUT_PSD32 (requires file extension to match).
    
    renderImage(...)
        Renders the scene to an image file.
        path = File path to render to. The extension dictates the image format (can be jpg/jpeg, png, exr, tif/tiff or psd). *
        width = Resolution width in pixels of the output image (default = scene width).
        height = Resolution height in pixels of the output image (default = scene height).
        opts = Options specified as a lux.RenderOptions object (see lux.getRenderOptions()).
        format = Image format. Can be one of the following values: lux.RENDER_OUTPUT_JPEG, lux.RENDER_OUTPUT_PNG, lux.RENDER_OUTPUT_EXR, lux.RENDER_OUTPUT_TIFF8, lux.RENDER_OUTPUT_TIFF32, lux.RENDER_OUTPUT_PSD8, lux.RENDER_OUTPUT_PSD16, lux.RENDER_OUTPUT_PSD32 (requires file extension to match).
    
    renderMultiMaterial(...)
        Renders a multi-material in the scene.
        name = The name of the material or multi-material to apply. It can also be an instance of lux.MultiMaterial. *
        folder = Folder to render files to. *
        opts = Options specified as a lux.RenderOptions object (see lux.getRenderOptions()).
    
    renderXR(...)
        Renders a XR from the scene.
        folder = Folder to put results in. *
        name = Name of the XR. *
        type = XR type. (default = lux.XR_TYPE_TURNTABLE)
        center = XR center type. (default = lux.XR_CENTER_OBJECT)
        width = Resolution width in pixels of the frames (default = scene width).
        height = Resolution height in pixels of the frames (default = scene height).
        vwidth = Viewport width in pixels. Will be the size that is displayed in XR. (default = resolution width).
        vheight = Viewport height in pixels. Will be the size that is displayed in XR. (default = resolution height).
        hframes = Horizontal frames. The XR type plays a role here. (default = 0 = use default)
        vframes = Vertical frames. The XR type plays a role here. (default = 0 = use default)
        hbegin = Horizontal angel begin. (only for lux.XR_TYPE_CUSTOM)
        hend = Horizontal angel end. (only for lux.XR_TYPE_CUSTOM)
        vbegin = Vertical angel begin. (only for lux.XR_TYPE_CUSTOM)
        vend = Vertical angel end. (only for lux.XR_TYPE_CUSTOM)
        opts = Explicit render options specified as a lux.RenderOptions object (see lux.getRenderOptions()). NOTE that some values are overwritten by other options provided to this function and internally to suite the XR rendering.
    
    saveCamera(...)
        Saves current camera if there are unsaved changes.
    
    saveFile(...)
        Saves scene to a file. If no path is given then known path is used or a dialog will ask in GUI mode while an exception is thrown in headless mode.
        path = File to save to.
        excludeFlags = A list of properties that can be filtered out. (default = empty)
        Allowed excludeFlags are lux.SAVE_EXCLUDE_CONFIGURATOR, lux.SAVE_EXCLUDE_STUDIOS, lux.SAVE_EXCLUDE_GEOMETRY, lux.SAVE_EXCLUDE_CAMERAS, lux.SAVE_EXCLUDE_ENVIRONMENTS, lux.SAVE_EXCLUDE_IMAGE_STYLES, lux.SAVE_EXCLUDE_NURBS and lux.SAVE_EXCLUDE_ANIMATIONS.
        Notice you need to exclude Configurator (if there is one) to exclude Studios.
        In order exclude something a studio can control both studios and configurator must be excluded. If that isn't done the exclude will not occur.
    
    saveMaterial(...)
        Save material to material library.
        name = Name of material to save. *
        folder = Relative folder to save to inside material library.
    
    saveMaterialMetadata(...)
        Persist the changes made to the metadata of a material.
        metadata = The metadata object on which the metadata properties have been updated. *
    
    saveMaterialPackage(...)
        Saves a material, including textures etc., to a file as a KMP.
        mat = The name of the material to save. *
        path = File to save to. *
    
    savePackage(...)
        Saves scene to a file as a KSP. If no path is given then known path is used or a dialog will ask in GUI mode while an exception is thrown in headless mode.
        path = File to save to.
        password = password for opening file (default = empty)
        viewerFlags = A list of properties flags when the file is opened in KeyShot viewer. (default = empty)
        Allowed viewerFlags are lux.KSP_VIEWER_SHOW_LOGO and lux.KSP_VIEWER_SHOW_WATERMARK.
        excludeFlags = A list of properties that can be filtered out. (default = empty)
        Allowed excludeFlags are lux.SAVE_EXCLUDE_CONFIGURATOR, lux.SAVE_EXCLUDE_STUDIOS, lux.SAVE_EXCLUDE_GEOMETRY, lux.SAVE_EXCLUDE_CAMERAS, lux.SAVE_EXCLUDE_ENVIRONMENTS, lux.SAVE_EXCLUDE_IMAGE_STYLES, lux.SAVE_EXCLUDE_NURBS and lux.SAVE_EXCLUDE_ANIMATIONS.
        Notice you need to exclude Configurator (if there is one) to exclude Studios.
        In order exclude something a studio can control both studios and configurator must be excluded. If that isn't done the exclude will not occur.
    
    screenshot(...)
        Take a screenshot of current real-time view state and return the path to it.
    
    setActiveColorway(...)
        Set active colorway of the scene. Use lux.getColorways() to get a list of names.
        colorway = colorway object. *
    
    setActiveEnvironment(...)
        Set active environment of the scene. Use lux.getEnvironments() to get a list of names.
        name = Name of the environment. *
    
    setActiveImageStyle(...)
        Set active image style of the scene. Use lux.getImageStyles() to get a list of names.
        name = Name of the image style. *
    
    setActiveStudio(...)
        Set active studio name of the scene.
        name = Name of studio. *
    
    setAnimationFrame(...)
        Set the animation frame.
        frame = The animation frame number. *
    
    setAnimationTime(...)
        Set the animation time in seconds.
        secs = The animation time in seconds as a floating-point number. *
    
    setCamera(...)
        Sets the active camera of the scene.
        camera = The name of the camera to use. *
    
    setCameraDirection(...)
        Sets the direction of the active camera of the scene.
        dir = Direction of the camera (x, y, z). Vector will be normalized. *
    
    setCameraDistance(...)
        Set distance from active camera to pivot/look-at point.
        dist = The distance. *
    
    setCameraFieldOfView(...)
        Sets the field of view of the active camera of the scene.
        deg = Field of view in degrees ]0, 180[. *
    
    setCameraFocalLength(...)
        Sets the focal length of the active camera of the scene.
        length = Focal length in mm [5, 200]. *
    
    setCameraLookAt(...)
        Set camera to look at an object or a point.
        obj = Object ID.
        pt = Point as tuple (x, y, z).
    
    setCameraOrthographic(...)
        Set the active camera of the scene to orthographic mode.
    
    setCameraPanoramic(...)
        Set the active camera of the scene to panoramic mode.
        type = Type of the panoramic mode. Must be one of the following: lux.PANORAMA_TYPE_SPHERICAL, lux.PANORAMA_TYPE_CUBEMAP. (default = lux.PANORAMA_TYPE_SPHERICAL)
    
    setCameraPerspective(...)
        Set the active camera of the scene to perspective mode.
    
    setCameraPosition(...)
        Sets the position of the active camera of the scene.
        pos = Position of the camera (x, y, z). *
    
    setCameraShift(...)
        Set the active camera of the scene to shift lens mode.
        vertical = sets the vertical shift of the lens (default not set).
        horizontal = sets the horizontal shift of the lens (default not set).
        estimate = optimizes parameters incl. vertical from the horizontal setting (default = false).
    
    setCameraUp(...)
        Sets the up vector of the active camera of the scene. Vector will be normalized.
        up = Up vector of the camera (x, y, z). *
    
    setKeepAspectRatio(...)
        Set whether aspect ratio is to be kept.
        keep = Keep aspect ratio. (default = True)
    
    setLightingPreset(...)
        Set lighting preset to be used.
        name = Name of preset. *
    
    setLockResolution(...)
        Set whether resolution is locked.
        lock = Lock resolution. (default = True)
    
    setMaterialTemplate(...)
        Applies a material template to part of the scene or all of it if no argument is given.
        name = Name of the material template. *
        showSel = Show part selection dialog. (only in GUI mode)
    
    setModelSets(...)
        Set active model sets and deativate all others. It returns true if all names of model sets could be activated, and thus false even if only some were activated.
        names = The list of names of model sets to activate. Using 'Default' will set the default model set. An empty list deactivates all model sets. *
    
    setObjectMaterial(...)
        Applies a material to an object in the scene.
        mat = Material name to apply. *
        obj = Object ID to apply to. *
        link = Whether to link to the material or create a duplicate. (default = False)
    
    setRenderEngine(...)
        Set render engine to use for the scene.
        engine = Type of render engine to use: lux.RENDER_ENGINE_PRODUCT, lux.RENDER_ENGINE_INTERIOR, lux.RENDER_ENGINE_PRODUCT_GPU, or lux.RENDER_ENGINE_INTERIOR_GPU. *
    
    setSceneUnit(...)
        Set scene unit and rescale scene if desired.
        unit = The scene unit can be one of the following values: lux.UNIT_MM, lux.UNIT_CM, lux.UNIT_IN, lux.UNIT_FT, lux.UNIT_M. *
        keep = Whether to keep current size or rescale (default = True).
    
    setSphericalCamera(...)
        Set spherical information of active camera: azimuth, inclination, and twist.
        azimuth = The spherical azimuth in degrees [-180, 180]. *
        incl = The spherical inclination in degrees [-90, 90]. *
        twist = The spherical twist degrees [-180, 180]. *
    
    setStandardView(...)
        Set standard view of currently active camera.
        view = Standard view to set. Must be one of the following: lux.VIEW_FRONT, lux.VIEW_BACK, lux.VIEW_LEFT, lux.VIEW_RIGHT, lux.VIEW_TOP, lux.VIEW_BOTTOM, lux.VIEW_ISOMETRIC. *
    
    setUndoEnabled(...)
        Enable or disable the undo/redo stack. When a script context is destroyed then undo is re-enabled if disabled.
        enable = Enable or not (default = true).
    
    sync(...)
        Synchronize event queue to enforce pending operations.
    
    unpause(...)
        Unpauses renderer.
DATA
    CAMERA_TYPE_ORTHOGRAPHIC = 65536
    CAMERA_TYPE_PANORAMA = 4096
    CAMERA_TYPE_PERSPECTIVE = 16384
    CAMERA_TYPE_PERSPECTIVE_STEREO = 32768
    CAMERA_TYPE_SHIFT = 8192
    CMF_KIND_COLOR_CMYK = 4
    CMF_KIND_COLOR_HEX = 6
    CMF_KIND_COLOR_LAB = 5
    CMF_KIND_COLOR_NAME = 2
    CMF_KIND_COLOR_RGB = 3
    CMF_KIND_COLOR_SWATCH = 7
    CMF_KIND_IMAGE = 1
    CMF_KIND_TEXT = 0
    DIALOG_CHECK = 4
    DIALOG_DOUBLE = 2
    DIALOG_FILE = 5
    DIALOG_FOLDER = 6
    DIALOG_INTEGER = 1
    DIALOG_ITEM = 3
    DIALOG_LABEL = 7
    DIALOG_TEXT = 0
    EXPORT_3MF = 5
    EXPORT_BAKING = 4
    EXPORT_FBX = 1
    EXPORT_GLTF = 2
    EXPORT_OBJ = 0
    EXPORT_OUTPUT_GEOMETRY_SHADERS = 1
    EXPORT_OUTPUT_TEXTURES = 0
    EXPORT_SINGLE_COLOR = 0
    EXPORT_STL = 4
    EXPORT_SUB_DIV_ADAPTIVE = 2
    EXPORT_SUB_DIV_EDGE_LENGTH = 1
    EXPORT_SUB_DIV_NORMAL = 1
    EXPORT_SUB_DIV_POLYCOUNT = 0
    EXPORT_USD = 6
    EXPORT_VERTEX_COLOR = 1
    FOLDER_ANIMATIONS = 8
    FOLDER_BACKPLATES = 3
    FOLDER_COLORS = 9
    FOLDER_CONFIG_ROOT = 14
    FOLDER_DOWNLOADS = 16
    FOLDER_ENVIRONMENTS = 5
    FOLDER_EXTERNAL_PLUGIN = 13
    FOLDER_FAVORITES = 11
    FOLDER_MATERIALS = 7
    FOLDER_MATERIAL_TEMPLATES = 10
    FOLDER_MODELS = 15
    FOLDER_RESOURCE_ROOT = 1
    FOLDER_SCENES = 6
    FOLDER_SCREENSHOTS = 2
    FOLDER_SCRIPTS = 12
    FOLDER_TEXTURES = 4
    IMAGE_STYLE_BASIC = 0
    IMAGE_STYLE_PHOTOGRAPHIC = 1
    KSP_VIEWER_SHOW_LOGO = 1
    KSP_VIEWER_SHOW_WATERMARK = 2
    MESSAGE_BOX_CRITICAL = 3
    MESSAGE_BOX_INFO = 1
    MESSAGE_BOX_WARNING = 2
    META_DATA_SIMPLE = 1
    META_DATA_XMP = 0
    MODEL_ID_CLOTH_DRAPE = 'ClothDrape_100x200_mm'
    MODEL_ID_CRYSTAL = 'Crystal'
    MODEL_ID_LIQUID_GLASS = 'LiquidGlass_60_mm'
    MODEL_ID_LUXION_SPHERE = 'LuxionSphere'
    MODEL_ID_MATERIAL_DISC_100_MM = 'MaterialDisc_100_mm'
    MODEL_ID_MATERIAL_DISC_1_M = 'MaterialDisc_1_m'
    MODEL_ID_MATERIAL_DISC_25_MM = 'MaterialDisc_25_mm'
    MODEL_ID_MATERIAL_DISC_TOON_100_MM = 'MaterialDiscToon_100_mm'
    MODEL_ID_SPHERE_CUTAWAY_100_MM = 'SphereCutaway_100_mm'
    NODE_TYPE_ANIMATION = 3
    NODE_TYPE_CAMERA = 6
    NODE_TYPE_GROUP = 1
    NODE_TYPE_MODEL = 5
    NODE_TYPE_MODEL_SET = 4
    NODE_TYPE_OBJECT = 2
    PANORAMA_TYPE_CUBEMAP = 1
    PANORAMA_TYPE_SPHERICAL = 0
    PARAMETER_TYPE_ANIMATIONCURVE = 17
    PARAMETER_TYPE_AXALTACOLOR = 18
    PARAMETER_TYPE_BOOLEAN = 1
    PARAMETER_TYPE_COLOR = 13
    PARAMETER_TYPE_COLORALPHA = 14
    PARAMETER_TYPE_COLORGRADIENT = 16
    PARAMETER_TYPE_DOUBLE = 7
    PARAMETER_TYPE_DOUBLE3 = 8
    PARAMETER_TYPE_FLOAT = 4
    PARAMETER_TYPE_FLOAT2 = 5
    PARAMETER_TYPE_FLOAT3 = 6
    PARAMETER_TYPE_FLOATARRAY = 15
    PARAMETER_TYPE_INTEGER = 2
    PARAMETER_TYPE_INTEGERLIST = 3
    PARAMETER_TYPE_MATRIX = 12
    PARAMETER_TYPE_SHADERBUMP = 65539
    PARAMETER_TYPE_SHADERGEOMETRY = 65540
    PARAMETER_TYPE_SHADERLABEL = 65538
    PARAMETER_TYPE_SHADERSURFACE = 65537
    PARAMETER_TYPE_SHADERUV = 65541
    PARAMETER_TYPE_STRING = 9
    PARAMETER_TYPE_STRINGLIST = 10
    PARAMETER_TYPE_WEAVEPATTERN = 19
    RENDER_ENGINE_INTERIOR = 1
    RENDER_ENGINE_INTERIOR_GPU = 4
    RENDER_ENGINE_PRODUCT = 0
    RENDER_ENGINE_PRODUCT_GPU = 3
    RENDER_MODE_ADVANCED = 0
    RENDER_MODE_SAMPLES = 2
    RENDER_MODE_TIME = 1
    RENDER_OUTPUT_EXR = 2
    RENDER_OUTPUT_JPEG = 0
    RENDER_OUTPUT_PNG = 5
    RENDER_OUTPUT_PSD16 = 8
    RENDER_OUTPUT_PSD32 = 7
    RENDER_OUTPUT_PSD8 = 6
    RENDER_OUTPUT_TIFF32 = 3
    RENDER_OUTPUT_TIFF8 = 1
    SAVE_EXCLUDE_ANIMATIONS = 128
    SAVE_EXCLUDE_CAMERAS = 8
    SAVE_EXCLUDE_CONFIGURATOR = 1
    SAVE_EXCLUDE_ENVIRONMENTS = 16
    SAVE_EXCLUDE_GEOMETRY = 4
    SAVE_EXCLUDE_IMAGE_STYLES = 32
    SAVE_EXCLUDE_NURBS = 64
    SAVE_EXCLUDE_STUDIOS = 2
    SHADER_TYPE_ADVANCED = 'lux_advanced'
    SHADER_TYPE_ANISOTROPIC = 'lux_anisotropic'
    SHADER_TYPE_AXALTA_PAINT = 'dupont_paint'
    SHADER_TYPE_BAKED_PLASTIC = 'lux_baked_plastic'
    SHADER_TYPE_BRUSHED = 'lux_brushed2'
    SHADER_TYPE_BRUSHED_RADIAL = 'lux_brushed_solid'
    SHADER_TYPE_BUBBLES = 'lux_bubbles'
    SHADER_TYPE_BUMP_ADD = 'lux_bumpmap_add'
    SHADER_TYPE_BUMP_TO_ROUGHNESS = 'lux_bump2roughness'
    SHADER_TYPE_CAMOUFLAGE = 'lux_camouflage'
    SHADER_TYPE_CELLULAR = 'lux_worley'
    SHADER_TYPE_COLOR_ADJUST = 'lux_color_adjust'
    SHADER_TYPE_COLOR_COMPOSITE = 'lux_color_blend'
    SHADER_TYPE_COLOR_FADE = 'animation_color'
    SHADER_TYPE_COLOR_GRADIENT = 'lux_color_gradient'
    SHADER_TYPE_COLOR_INVERT = 'lux_color_invert'
    SHADER_TYPE_COLOR_KEY_MASK = 'lux_color_distance'
    SHADER_TYPE_COLOR_TO_NUMBER = 'convert_rgba_to_float'
    SHADER_TYPE_CONTOUR = 'lux_contour_tex'
    SHADER_TYPE_CURVATURE = 'lux_curvature'
    SHADER_TYPE_CURVE_COLOR_RANDOMIZE = 'lux_curve_randomize'
    SHADER_TYPE_CURVE_FADE = 'animation_curve'
    SHADER_TYPE_CUTAWAY = 'lux_cutaway'
    SHADER_TYPE_DIELECTRIC = 'lux_glass'
    SHADER_TYPE_DIFFUSE = 'lux_diffuse'
    SHADER_TYPE_DISPLACE = 'lux_displace'
    SHADER_TYPE_EMISSIVE = 'lux_emissive'
    SHADER_TYPE_FIBER_WEAVE = 'lux_carbon'
    SHADER_TYPE_FLAKES = 'lux_flakes'
    SHADER_TYPE_FLAT = 'lux_constant'
    SHADER_TYPE_FUZZ = 'lux_fuzz'
    SHADER_TYPE_GEM = 'lux_gem'
    SHADER_TYPE_GENERAL = 'lux_general'
    SHADER_TYPE_GENERIC = 'lux_generic'
    SHADER_TYPE_GLASS = 'lux_window_glass'
    SHADER_TYPE_GLASS_SOLID = 'lux_glass_simple'
    SHADER_TYPE_GRANITE = 'lux_granite'
    SHADER_TYPE_GROUND = 'lux_ground'
    SHADER_TYPE_IES_LIGHT = 'lux_ies_light'
    SHADER_TYPE_LEATHER = 'lux_leather_tex'
    SHADER_TYPE_LIQUID = 'lux_liquid'
    SHADER_TYPE_MAPPING_2D = 'mapping2d'
    SHADER_TYPE_MAPPING_WARP = 'lux_mapping_warp'
    SHADER_TYPE_MARBLE = 'lux_marble'
    SHADER_TYPE_MATCAP = 'matcap'
    SHADER_TYPE_MEASURED = '__measured'
    SHADER_TYPE_MESH = 'lux_mesh'
    SHADER_TYPE_MESH_CIRCULAR = 'lux_lattice_circular'
    SHADER_TYPE_MESH_LIGHT = 'lux_mesh_light'
    SHADER_TYPE_MESH_POLYGON = 'lux_lattice_polygon'
    SHADER_TYPE_METAL = 'lux_metal'
    SHADER_TYPE_METALLIC_PAINT = 'metallic_paint'
    SHADER_TYPE_MOLD_TECH_PLASTIC = 'lux_moldtech_plastic'
    SHADER_TYPE_NOISE_FRACTAL = 'lux_fractal_noise'
    SHADER_TYPE_NOISE_TEXTURE = 'lux_noise'
    SHADER_TYPE_OCCLUSION = 'lux_occlusion_tex'
    SHADER_TYPE_PAINT = 'lux_paint'
    SHADER_TYPE_PLASTIC = 'lux_plastic_simple'
    SHADER_TYPE_PLASTIC_CLOUDY = 'lux_cloudy_plastic'
    SHADER_TYPE_PLASTIC_FIBER = 'lux_textile_fiber'
    SHADER_TYPE_PLASTIC_TRANSPARENT = 'lux_plastic'
    SHADER_TYPE_POINT_LIGHT = 'lux_point_light'
    SHADER_TYPE_RAY_MASK = 'lux_ray_mask'
    SHADER_TYPE_REALCLOTH = 'lux_real_cloth'
    SHADER_TYPE_ROUNDED_EDGES = 'lux_rounded'
    SHADER_TYPE_SCATTERING_MEDIUM = 'lux_scattering_medium'
    SHADER_TYPE_SCRATCHES = 'lux_scratches_worley'
    SHADER_TYPE_SPOTLIGHT = 'lux_spotlight'
    SHADER_TYPE_SPOTS = 'lux_spots'
    SHADER_TYPE_TEXTURE_MAP = '__texture'
    SHADER_TYPE_THIN_FILM = 'lux_thinfilm'
    SHADER_TYPE_TILED_UV = 'lux_tiled_texturemap'
    SHADER_TYPE_TOON = 'lux_toon'
    SHADER_TYPE_TRANSLUCENT = 'lux_translucent'
    SHADER_TYPE_TRANSLUCENT_ADVANCED = 'lux_translucent2'
    SHADER_TYPE_TRANSLUCENT_MEDIUM = 'lux_translucent_mc'
    SHADER_TYPE_TRI_PLANAR = 'triplanar'
    SHADER_TYPE_VELVET = 'lux_velvet'
    SHADER_TYPE_VERTEX_COLOR = 'lux_vertex_color'
    SHADER_TYPE_VIDEO_MAP = 'sequence_rgba'
    SHADER_TYPE_VOLUME_MAP = 'lux_volume'
    SHADER_TYPE_WEAVE = 'lux_weave2'
    SHADER_TYPE_WIREFRAME = 'show_wireframe'
    SHADER_TYPE_WOOD = 'lux_wood'
    SHADER_TYPE_WOOD_ADVANCED = 'lux_wood2'
    SHADER_TYPE_XRAY = 'lux_xray'
    UNIT_CM = 1
    UNIT_FT = 3
    UNIT_IN = 2
    UNIT_M = 4
    UNIT_MM = 0
    VIEW_BACK = 2
    VIEW_BOTTOM = 6
    VIEW_FRONT = 1
    VIEW_ISOMETRIC = 7
    VIEW_LEFT = 3
    VIEW_RIGHT = 4
    VIEW_TOP = 5
    XR_CENTER_CAMERA = 4
    XR_CENTER_CAMERA_PIVOT = 5
    XR_CENTER_ENVIRONMENT = 1
    XR_CENTER_OBJECT = 2
    XR_TYPE_CUSTOM = 5
    XR_TYPE_HEMISPHERICAL = 3
    XR_TYPE_SPHERICAL = 2
    XR_TYPE_TUMBLE = 4
    XR_TYPE_TURNTABLE = 1
FILE
    (built-in)

```
