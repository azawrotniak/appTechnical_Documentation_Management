from django.db import models

TYPE_MACHINE = (
    (1, "Milling"),
    (2, "Lathe"),
)


class Service(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True)
    tax_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True, null=True)
    tax_number = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name


class Machine(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.CharField(max_length=64)
    type = models.IntegerField(choices=TYPE_MACHINE)
    serial_number = models.CharField(max_length=64)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tool(models.Model):
    name = models.CharField(max_length=64)
    kind = models.CharField(max_length=32)
    size = models.DecimalField(max_digits=4, decimal_places=2)
    number_tiles = models.IntegerField()
    height = models.DecimalField(max_digits=5, decimal_places=1)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=64)
    symbol = models.CharField(max_length=32)

    @property
    def material_name(self):
        return "{} {}".format(self.name, self.symbol)

    def __str__(self):
        return self.material_name


class Element(models.Model):
    name = models.CharField(max_length=64)
    version = models.IntegerField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    tool = models.ManyToManyField(Tool)

    def __str__(self):
        return self.name
