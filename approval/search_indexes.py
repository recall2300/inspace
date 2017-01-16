import datetime
from haystack import indexes
from approval.models import Approval


class ApprovalIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    department = indexes.CharField(model_attr='department')
    reason = indexes.CharField(model_attr='reason')
    start_date = indexes.DateTimeField(model_attr='start_date')

    def get_model(self):
        return Approval

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(start_date__lte=datetime.datetime.now())
