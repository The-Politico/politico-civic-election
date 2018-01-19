from django.db import models


class ElectionType(models.Model):
    """
    e.g., "General", "Primary"
    """
    uid = models.CharField(
        max_length=500,
        primary_key=True,
        editable=False,
        blank=True)

    slug = models.SlugField(
        blank=True, max_length=255, unique=True
    )
    label = models.CharField(max_length=255, blank=True)
    short_label = models.CharField(max_length=50, null=True, blank=True)

    ap_code = models.CharField(max_length=1)
    is_general = models.BooleanField(default=False)
    primary_type = models.CharField(max_length=50, null=True, blank=True)
    number_of_winners = models.PositiveSmallIntegerField(default=1)
    winning_threshold = models.DecimalField(
        decimal_places=3, max_digits=5, null=True, blank=True)

    def __str__(self):
        return self.uid

    def save(self, *args, **kwargs):
        """
        **uid**: :code:`electiontype:{name}`
        """
        self.uid = 'electiontype:{}'.format(self.slug)
        super(ElectionType, self).save(*args, **kwargs)
