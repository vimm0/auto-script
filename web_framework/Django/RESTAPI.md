Writable Nested Serializer

```

class Attendance(models.Model):
    reference = models.CharField(max_length=8, blank=True, null=True, editable=False)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now)
    created = models.DateTimeField(auto_now_add=True)
    by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "Attendance of {}-{}".format(self.level, self.date.strftime('%B %d, %Y'))

    class Meta:
        unique_together = (('level', 'date'),)


class AttendanceRecord(models.Model):
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, choices=ATTENDANCE_STATUS)
    note = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.status)

```


```
class AttendanceRecordSerializer(serializers.ModelSerializer):
    # make just like subject mark
    class Meta:
        model = AttendanceRecord
        fields = [f.name for f in AttendanceRecord._meta.fields if f.name not in attendanceRecordFilter]
        extra_kwargs = {
            'attendance': {'read_only': True}
        }


class AttendanceSerializer(WritableNestedModelSerializer):
    attendancerecord_set = AttendanceRecordSerializer(many=True, read_only=False)

    class Meta:
        model = Attendance
        fields = [f.name for f in Attendance._meta.fields if f.name not in globalFilter] + ['__str__',
                                                                                            'reference',
                                                                                            'attendancerecord_set',
                                                                                            'by',
                                                                                            'academic_year']
        order_by = (('attendancerecord_set',))  # orders attendancerecord_set (while update)

```

```
def create(self, validated_data):
        attendancerecord_data = validated_data.pop('attendancerecord_set')
        attendance = Attendance.objects.create(**validated_data)
        for ar in attendancerecord_data:
            AttendanceRecord.objects.create(attendance=attendance, **ar)
        return attendance

def update(self, instance, validated_data):
    """
    :param instance:
    :param validated_data:
    :return:
    """
    level = validated_data.pop('level')
    description = validated_data.pop('academic_year')
    date = validated_data.pop('date')
    by = validated_data.pop('by')
    attendancerecord_data = validated_data.pop('attendancerecord_set')

    instance.level = level
    instance.description = description
    instance.date = date
    instance.by = by
    instance.save()

    attendancerecords = instance.attendancerecord_set.all()
    attendancerecords = list(attendancerecords)

    for a in attendancerecord_data:
        if attendancerecords:
            attendancerecord = attendancerecords.pop(0)
            attendancerecord.attendance = a.get('attendance', attendancerecord.attendance)
            attendancerecord.student = a.get('student', attendancerecord.student)
            attendancerecord.status = a.get('status', attendancerecord.status)
            attendancerecord.note = a.get('note', attendancerecord.note)
            attendancerecord.save()
        else:
            instance.attendancerecord_set.update_or_create(
                student=a.get('student', None), status=a.get('status', None), note=a.get('note', None))
    return instance

```
But [https://github.com/beda-software/drf-writable-nested](https://github.com/beda-software/drf-writable-nested) could be used for writable nested serializer.

Reference:
  - [https://django.cowhite.com/blog/create-and-update-django-rest-framework-nested-serializers/](https://django.cowhite.com/blog/create-and-update-django-rest-framework-nested-serializers/)
