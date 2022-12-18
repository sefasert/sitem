from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver  #receiver decoratörü kütüphanesini getir
from .models import Account, UserProfile

@receiver(post_save, sender=Account)  #receiver decoratör connect şekli en yaygın kullanım
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:                                    #eğer UserProfile True ise
        UserProfile.objects.create(user=instance) #User oluşur-oluşmaz UserProfile boş email şekilde oluşacaktır
        print("user profile is created")          #print'e yazdır

    else:                                           # eğer UserProfile False ise (try-except aç)
        try:
            profile = UserProfile.objects.get(user=instance) #oluşan User'ın UserProfile'sinin emailini güncelle
            profile.save()
        except:  #UserProfile yoksa, oluşturulan User'ı save et otomatik olarak UserProfile oluşcak
            UserProfile.objects.create(user=instance)
            print("profile was not exist, but I created one")
        print("user is updated")

# post_save_connect(post_save_create_profile_receiver, sender=User) #diğer connect şekli

@receiver(pre_save, sender=Account)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(instance.username, "this user is get saved") #User oluştur yada güncelle, en önce console'da burası yazar

# post_save_connect(pre_save_profile_receiver, sender=User)
