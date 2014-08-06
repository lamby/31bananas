from django_enumfield import Enumeration, Item

class StateEnum(Enumeration):
    DRAFT       = Item(10, 'draft', "Draft")
    TASTED      = Item(20, 'tasted', "Tasted")
    PUBLISHED   = Item(30, 'published', "Published")
