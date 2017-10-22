from django.db import models

class Stock(models.Model):
	stock_ticker_sym = models.CharField(max_length=4)
	stock_name = models.CharField(max_length=200)
	curr_price = models.DecimalField(default=0.0, max_digits=999, decimal_places=2)
	purc_price = models.DecimalField(default=0.0, max_digits=999, decimal_places=2)
	share_number = models.DecimalField(default=0.0, max_digits=999, decimal_places=2)
	last_update = models.DateTimeField('last updated')
	purc_date = models.DateTimeField('purchase date')
	price_diff = models.DecimalField(default=0.0, max_digits=999, decimal_places=2)

	def __str__(self):
		return self.stock_ticker_sym


