from datetime import date

from django import forms



class BuscaRelatorioForm(forms.Form):

	ANOS_CHOICES = ()

	MESES_CHOICES = (
	    ('1', 'Janeiro'),
	    ('2', 'Fevereiro'),
	    ('3', 'Março'),
	    ('4', 'Abril'),
	    ('5', 'Maio'),
	    ('6', 'Junho'),
	    ('7', 'Julho'),
	    ('8', 'Agosto'),
	    ('9', 'Setembro'),
	    ('10', 'Outubro'),
	    ('11', 'Novembro'),
	    ('12', 'Dezembro'),
	)

	def __init__(self, vinculos, *args, **kwargs):
		super(BuscaRelatorioForm, self).__init__(*args, **kwargs)		

		#Propopular listagem de anos
		for ano in range(2017, date.today().year + 1):
			self.ANOS_CHOICES += (((str(ano), str(ano))),)

		self.fields['ano'] = forms.ChoiceField(
								label='Ano',
								required=True,
								choices=self.ANOS_CHOICES)

		#Popular listagem de vínculos		
		self.fields['bolsista'] = forms.ModelChoiceField(
									required=False, 
									queryset=vinculos,
									empty_label='Selecione o bolsista')

		#Valores iniciais		
		self.initial['mes'] = date.today().month
		self.initial['ano'] = date.today().year
	
	mes = forms.ChoiceField(
		label='Mês',
		required=True,
		choices=MESES_CHOICES,
	)
