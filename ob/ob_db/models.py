from django.db import models


class AynuData(models.Model):
    order = models.IntegerField("序")
    glyph_font = models.CharField("字形", max_length=255)
    glyph_image = models.ImageField("图片", upload_to="images/glyph/")
    liding = models.CharField("隶定", max_length=255)
    piece_number = models.CharField("甲骨片号", max_length=255)
    piece_image = models.ImageField("甲骨片图", upload_to="images/piece/")
    piece_filter = models.CharField("甲骨片滤镜", max_length=255)
    gulin_page = models.CharField("诂林页码", max_length=255)
    gulinbu_page = models.CharField("诂林补页码", max_length=255)
    jiabian_page = models.CharField("甲编页码", max_length=255)
    xinjiabian_page = models.CharField("新甲编页码", max_length=255)
    comment = models.TextField("备注", max_length=255)
    annotation = models.TextField("标注")

    def __str__(self):
        if self.annotation is not None:
            return f"<AYNU #{self.order}: {self.annotation}>"
        return f"<AYNU #{self.order}>"


class ZjnuData(models.Model):
    order = models.IntegerField("序")
    zjnu_font = models.CharField("浙师大字形", max_length=255)
    glyph_font = models.CharField("辞类编字形", max_length=255)
    glyph_image = models.ImageField("辞类编图片", upload_to="images/glyph/")
    liding = models.CharField("隶定", max_length=255)
    piece_image = models.ImageField("甲骨片图", upload_to="images/piece/")
    piece_filter = models.CharField("甲骨片滤镜", max_length=255)
    glyph_number = models.CharField("辞类编编号", max_length=255)
    comment = models.TextField("备注", max_length=255)
    annotation = models.TextField("标注")

    def __str__(self):
        if self.annotation is not None:
            return f"<ZJNU #{self.order}: {self.annotation}>"
        return f"<ZJNU #{self.order}>"


class FzData(models.Model):
    order = models.IntegerField("序")
    glyph = models.CharField("字形", max_length=255)
    liding = models.CharField("隶定", max_length=255)
    comment = models.TextField("备注", max_length=255)
    annotation = models.TextField("标注")

    def __str__(self):
        if self.annotation is not None:
            return f"<FZ #{self.order}: {self.annotation}>"
        return f"<FZ #{self.order}>"


class GulinData(models.Model):
    order = models.IntegerField("序")
    mojikyo_font = models.CharField("文字镜字形", max_length=255)
    shencao_font = models.CharField("文字镜字形", max_length=255)
    gulin_font = models.CharField("诂林字形", max_length=255)
    gulin_number = models.CharField("诂林编号", max_length=255)
    liding = models.CharField("隶定", max_length=255)
    comment = models.TextField("备注", max_length=255)
    annotation = models.TextField("标注")

    def __str__(self):
        if self.annotation is not None:
            return f"<Gulin #{self.order}: {self.annotation}>"
        return f"<Gulin #{self.order}>"


class OracularData(models.Model):
    order = models.IntegerField("序")
    glyph = models.CharField("字形", max_length=255)
    liding = models.CharField("隶定", max_length=255)
    jiabian_page = models.CharField("甲编页码", max_length=255)
    xinjiabian_page = models.CharField("新甲编页码", max_length=255)
    gulin_number = models.CharField("诂林编号", max_length=255)
    comment = models.TextField("备注", max_length=255)
    annotation = models.TextField("标注")

    def __str__(self):
        if self.annotation is not None:
            return f"<Oracular #{self.order}: {self.annotation}>"
        return f"<Oracular #{self.order}>"
