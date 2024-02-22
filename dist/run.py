class List(models.Model):
    title = models.CharField(max_length=200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    pincode = models.CharField(max_length = 20)
    description = models.TextField(blank = True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField(default = 0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=2)
    pic = models.ImageField(upload_to = 'photos/%Y/%m/%d/')
    pic_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    pic_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    pic_3 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    pic_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    pic_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/', blank = True)
    is_published = models.BooleanField(default = True)
    list_date = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        return self.title

https://visualstudio.microsoft.com/visual-cpp-build-tools/