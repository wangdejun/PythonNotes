from django.core.management.base import BaseCommand
from search import helper
import time
from product.models import Product

# a little piece of code from the working object for the purpose of Learning
# Its is a nearly perfect code and a model routine code to hanle command using in django:
# builtin command and function in django

class Command(BaseCommand):
       def handle(self, *args, **options):
        # a const value before the loop
        amount = 1000
        # keep loop and loop
        while True:
            print ('==========updating=========')
            products = Product.objects.select_related(
                'designer').filter(changed=True).order_by('-id')[0:ammount]
            #get the real number of the products meet the requirement
            count = products.count()
            print "Changed products to update: %s" %count
            # if the number is 0, no good,please have a rest for 30seconds
            if count==0:
                print "Sleep and Skip"
                time.sleep(30)
                continue
            #get the update and deletes counts from a function-return-value at the same time;
            update,deletes = helper.import_products(products)
            #print these lovely nums
            print 'Updated products %s' % updates
            print "Deleted products %s" % deletes
            #new a empty array and fill it with products' ids
            id = []
            for product in products:
                ids.append(product.id)
            
            #update it
            Product.objects.filter(id__in = ids).update(changed = 0)
            #break;

            if count<amount:
                print "Sleep"
                time.sleep(30)
                continue