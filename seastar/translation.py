from modeltranslation.translator import TranslationOptions, translator


from .models import  Welcome  , Product  ,Comment





class WelcomeTranslationOptions(TranslationOptions):
    fields = ("title","info",)




class CommentTranslationOptions(TranslationOptions):
    fields = ("info",)




class ProductTranslationOptions(TranslationOptions):
    fields = ("title","info",)





translator.register(Welcome,WelcomeTranslationOptions)
translator.register(Comment,CommentTranslationOptions)
translator.register(Product,ProductTranslationOptions)


