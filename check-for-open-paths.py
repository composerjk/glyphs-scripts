#MenuTitle: Check for open paths in selected glyphs
"""
Checks for open paths in selected glyphs (or all glyphs if no selection).
Output appears in Macro Window (Option-Command-M).
"""
# FIXME: test with masters and instances -- may not work

Font = Glyphs.font
Doc = Glyphs.currentDocument
selectedGlyphs = [ x.parent for x in Doc.selectedLayers() ]
selectedNames = [ x.name for x in selectedGlyphs ]
nopenpaths = 0
checkedGlyphs = []
print "Font: ", Font.familyName
if not selectedGlyphs:
	selectedGlyphs = Font.glyphs
	selectedNames = "all glyphs."
for glyph in selectedGlyphs:
	# assumption: glyph layer 0 without paths means glyph doesn't have any drawing in it, yet
	if glyph.layers[0].paths:
		checkedGlyphs.append(glyph.name)
		layers = glyph.layers	
		for layer in layers:
			paths = layer.paths
			for path in paths:
				if not path.closed:
					print "OPEN PATH: %s (%s)" % (layer.parent.name, layer.parent.unicode), "[layer: %s]" % layer.name, path
					nopenpaths += 1
if not nopenpaths:
	print "No open paths in %d glyphs:" % len(checkedGlyphs), checkedGlyphs
else:
	print "Total open paths: %d out of %d checked glyphs." % (nopenpaths, len(checkedGlyphs))
