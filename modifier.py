from xmlutils import *
from packitem import PackItem



class Modifier(PackItem):

    TAG = 'Modifier'

    def __init__(self):
        super(Modifier, self).__init__()
        self.type = None
        self.dtl = None
        self.value = 0
        self.text = ''

    @classmethod
    def build_from_xml(cls, elem):
        f = cls()
        cls.fill_from_xml(f, elem)
        return f

    @classmethod
    def fill_from_xml(cls, obj, elem):
        obj.type = read_attribute(elem, 'type')
        obj.dtl = read_attribute(elem, 'dtl')
        obj.value = read_attribute(elem, 'value')
        obj.text = elem.text

    @classmethod
    def build_list_from_xml(cls, elem):
        result = []
        if elem:
            for i_elem in elem.iter():
                if i_elem.tag == cls.TAG:
                    result.append(cls.build_from_xml(i_elem))
        return result

    def write_into(self, elem):
        pass
