from django.db import models
import django.utils.timezone as timezone


class User(models.Model):
    SEX_TYPE = (
        ('W', 'Woman'),
        ('M', 'Man')
    )
    username = models.CharField('账户', max_length=30)
    password = models.CharField('密码', max_length=30)
    nickname = models.CharField('昵称', max_length=30)
    sex = models.CharField('性别', max_length=1, choices=SEX_TYPE)
    join_time = models.DateTimeField('注册时间', default=timezone.now)
    introduction = models.TextField('自我介绍', null=True)
    head_path = models.CharField('头像路径', max_length=255, null=True)
    enjoy_music = models.CharField('喜欢的音乐', max_length=255, null=True)
    occupation = models.CharField('职业', max_length=100, null=True)
    address = models.CharField('所在地', max_length=100, null=True)
    native_place = models.CharField('籍贯', max_length=20, null=True)
    email = models.CharField('邮箱', max_length=60, null=True)
    enjoy = models.TextField('兴趣爱好', null=True)

    class Meta:
        app_label = "blog"


class Article(models.Model):
    ART_TYPE = (
        ('W', 'Woman'),
        ('M', 'Man')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=100)
    content = models.TextField('正文')
    create_time = models.DateTimeField('创建时间', default=timezone.now)
    revise_time = models.DateTimeField('修改时间', null=True)
    type = models.CharField('文章类型', max_length=1, choices=ART_TYPE)

    class Meta:
        app_label = "blog"


class ArticleReply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_time = models.DateTimeField('回复时间', default=timezone.now)
    content = models.TextField('回复内容')


class ArticleComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    parent = models.ForeignKey(ArticleReply, on_delete=models.CASCADE)
    comment_time = models.DateTimeField('评论时间', default=timezone.now)
    content = models.TextField('评论内容')
