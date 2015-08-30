import bpy
from ... base_types.node import AnimationNode

class TextSequenceOutputNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_TextSequenceOutputNode"
    bl_label = "Text Sequence Output"

    def create(self):
        self.inputs.new("an_SequenceSocket", "Sequence", "sequence").defaultDrawType = "PROPERTY_ONLY"
        self.inputs.new("an_StringSocket", "Text", "text")
        self.inputs.new("an_IntegerSocket", "Size", "size").number = 200
        self.inputs.new("an_BooleanSocket", "Shadow", "shadow").value = False
        socket = self.inputs.new("an_StringSocket", "Align", "align")
        socket.useEnum = True
        socket.setEnumItems([("CENTER", "Center"), ("LEFT", "Left"), ("RIGHT", "Right")])
        socket.string = "CENTER"
        self.inputs.new("an_FloatSocket", "X Location", "xLocation").number = 0.5
        self.inputs.new("an_FloatSocket", "Y Location", "yLocation").number = 0.0
        self.outputs.new("an_SequenceSocket", "Sequence", "outSequence")

    def execute(self, sequence, text, size, shadow, align, xLocation, yLocation):
        if getattr(sequence, "type", "") != "TEXT": return sequence

        sequence.text = text
        sequence.font_size = size
        sequence.use_shadow = shadow
        sequence.location[0] = xLocation
        sequence.location[1] = yLocation
        if align in ("CENTER", "LEFT", "RIGHT"):
            sequence.align = align

        return sequence
