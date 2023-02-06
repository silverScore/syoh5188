from django.db import models

# Create your models here.
# projects/silverScore/care/data/rankStatusData.csv
class CareRank(models.Model):
    ratingCd = models.CharField(max_length=15)
    longTermAdminCd = models.CharField(max_length=15)
    longTermAdminNm = models.CharField(max_length=100)
    adminPttnName = models.CharField(max_length=20)
    siDoName = models.CharField(max_length=20, blank=True, null=True)
    siGunGuName = models.CharField(max_length=20, blank=True, null=True)
    ratingDate = models.DateField(blank=True, null=True)
    ratingGrade = models.CharField(max_length=1, blank=True, null=True)
    opRating = models.IntegerField(blank=True, null=True)
    safeRating = models.IntegerField(blank=True, null=True)
    rightRating = models.IntegerField(blank=True, null=True)
    processRating = models.IntegerField(blank=True, null=True)
    resultRating = models.IntegerField(blank=True, null=True)

    # admin에서 보이기 위함
    def __str__(self):
        return f"기관명 : {self.longTermAdminNm} / 기관기호 : {self.longTermAdminCd}"

# projects/silverScore/care/data/addressNumbers.csv
class AddressInfo(models.Model):
    regionCd = models.IntegerField(blank=True, null=True)
    regionNm = models.CharField(max_length=200, blank=True, null=True)
    siDoNm = models.CharField(max_length=10, blank=True, null=True)
    siGunGuNm = models.CharField(max_length=10, blank=True, null=True)
    umdNm = models.CharField(max_length=10, blank=True, null=True)
    riNm = models.CharField(max_length=10, blank=True, null=True)
    siDoCd = models.IntegerField(blank=True, null=True)
    siGunGuCd = models.IntegerField(blank=True, null=True)
    DongCd = models.IntegerField(blank=True, null=True)
    riCd = models.IntegerField(blank=True, null=True)
    
    # admin에서 보이기 위함
    def __str__(self):
        return f"법정동코드 : {self.regionCd} / 지역명 : {self.regionNm}"
