import datetime
from haystack import indexes
from approval.models import Note


class NoteIndex(indexes.SearchIndex, indexes.Indexable):
    # Every SearchIndex requires there be one (and only one) field with document=True.
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='user')
    pub_date = indexes.DateTimeField(model_attr='pub_date')

    def get_model(self):
        return Note

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())