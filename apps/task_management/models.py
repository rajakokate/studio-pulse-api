from django.db import models
from apps.user_management.models import  Department
from django.conf import settings

# ------------------ Client (Assumed based on FK) ------------------
class Client(models.Model):
    clientID = models.CharField(primary_key=True, max_length=100)
    name = models.TextField()

    def __str__(self):
        return self.name


# ------------------ Project ------------------
class Project(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'TODO'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('IN REVIEW', 'IN REVIEW'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]

    projectID = models.AutoField(primary_key=True)
    projectName = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="TODO")
    dueDate = models.DateTimeField(blank=True, null=True)
    startDate = models.DateTimeField(blank=True, null=True)
    clientID = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    dept =  models.ForeignKey(Department, on_delete=models.CASCADE, null=True)
    description = models.TextField(null=True)
    def __str__(self):
        return self.ProjectName


# ------------------ ProjectComment ------------------
class ProjectComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Comment {self.commentId} on {self.project}"


# ------------------ Shot ------------------
class Shot(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'TODO'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('IN REVIEW', 'IN REVIEW'),
        ('APPROVED', 'APPROVED'),
        ('REJECTED', 'REJECTED'),
    ]

    shotId = models.IntegerField()
    ProjectId = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='shots')
    Status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    reel = models.TextField(blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)
    scene = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = (('shotId', 'ProjectId'),)

    def __str__(self):
        return f"Shot {self.shotId} - {self.ProjectId}"


# # ------------------ ShotAssociation ------------------
class ShotAssociation(models.Model):
    id = models.AutoField(primary_key=True)  # Add this line
    version = models.FloatField(default=1.0)
    shot = models.ForeignKey(Shot, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shot_assigned_to'
    )
    assigned_from = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='shot_assigned_from'
    )
    assignedDate = models.TextField(null=True, blank=True)
    dueDate = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('version', 'shot', 'user')


# # ------------------ Comment ------------------
class Comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    version = models.FloatField()
    shot_association = models.ForeignKey(ShotAssociation, on_delete=models.CASCADE)
    comment = models.TextField()

#     class Meta:
#         constraints = [
#             models.ForeignKey(
#                 'ShotAssociation',
#                 on_delete=models.CASCADE,
#                 db_constraint=False,
#                 to_field=('version', 'shot', 'user', 'dept'),
#             )
#         ]

    def __str__(self):
        return f"Comment {self.commentId} by {self.user}"