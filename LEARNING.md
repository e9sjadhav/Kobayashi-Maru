- signal wasn't registered in apps.py it didn't work.

- used this to save objects again to trigger signal

```for t in TeamMatch.objects.all():
        t.save()
```

- url order matters in urlspatterns, django will try to match urls in whatever order are passed

```
teams/<str:team_name>,
teams/matches/
```

- so when the query paramater passed for 2nd url will be used by 1st url considering it as parameter for 1st url
- so always keep those urls below like this

```
teams/matches/
teams/<str:team_name>,
```

### fixtures

```
python manage.py dumpdata tournament > fixtures/tournament.json
```

### contenttype

- Django includes a contenttypes application that can track all of the models installed in your Django-powered project

- created auditlog with default feilds like content_type, object_id, content_object

  - There are three parts to setting up a GenericForeignKey:
  - Give your model a ForeignKey to ContentType. The usual name for this field is “content_type”.
  - Give your model a field that can store primary key values from the models you’ll be relating to. For most models, this means a PositiveBigIntegerField. The usual name for this field is “object_id”.
  - Give your model a GenericForeignKey, and pass it the names of the two fields described above. If these fields are named “content_type” and “object_id”, you can omit this – those are the default field names GenericForeignKey will look for.

  - generic relations:
  - Adding a foreign key from one of your own models to ContentType allows your model to effectively tie itself to another model class
  - A normal ForeignKey can only “point to” one other model, which means that if the AuditLog model used a ForeignKey it would have to choose one and only one model to store tags for. The contenttypes application provides a special field type (GenericForeignKey) which works around this and allows the relationship to be with any model:

- Reverse generic relations
- these can be reverse genereic relation.
- The relation on the related object back to this object doesn’t exist by default.

```
log = GenericRelation(AuditLog)
```

##

```
def get_queryset(self):
        term = self.kwargs["term"]
        if term:
            return self.model.objects.filter(body__icontains=term)
        return self.model.objects.none()
```
