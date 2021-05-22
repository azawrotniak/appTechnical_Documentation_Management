from django.db import models

TYPE_DOCUMENT = (
    (1, "Drawing"),
    (2, "Document"),
    (3, "G-code"),
)

TYPE_MACHINE = (
    (1, "Milling"),
    (2, "Lathe"),
)

STATUS = (
    (1, "Active"),
    (2, "Inactive"),
)


class Service(models.Model):
    """
    The model represents the service company
    """
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True)
    tax_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    """
    The model represents a company that supplies machines, tools, materials, etc.
    """
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True, null=True)
    tax_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Machine(models.Model):
    """
    The model represents a CNC machine.
    """
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    type = models.IntegerField(choices=TYPE_MACHINE)
    serial_number = models.CharField(max_length=64)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tool(models.Model):
    """
    The model represents the tools needed for machining, e.g. drills, cutters, drills, chamfers, etc.
    """
    name = models.CharField(max_length=64)
    status = models.IntegerField(choices=STATUS, default=1, blank=True)
    kind = models.CharField(max_length=32)
    size = models.DecimalField(max_digits=4, decimal_places=2)
    number_tiles = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=1)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Material(models.Model):
    """
    The model represents the material needed to manufacture the element eg. steel, aluminium etc.
    """
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=32)

    @property
    def material_name(self):
        return "{} {}".format(self.name, self.symbol)

    def __str__(self):
        return self.material_name


class Element(models.Model):
    """
    The model represents the element that is being manufactured.
    """
    name = models.CharField(max_length=64)
    version = models.IntegerField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    tool = models.ManyToManyField(Tool)
    model3D = models.FileField(upload_to='models/', blank=True)

    def __str__(self):
        return self.name


class Attachment(models.Model):
    """
    The model represents an attachment which is a help set of information to create an element
    """
    description = models.CharField(max_length=64, blank=True)
    type = models.IntegerField(choices=TYPE_DOCUMENT, blank=True)
    file = models.FileField(upload_to='documents/', blank=True)
    element = models.ForeignKey(Element, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.description
