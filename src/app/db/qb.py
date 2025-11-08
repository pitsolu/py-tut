import camelsnake

# from src.app.db.base import *

###
# Query Builder
###
class Qb:
	def __init__(self, model):
		self.predicates = []
		self.fields = []
		self.joins = []
		self.aggr = camelsnake.camel_to_snake(model.__name__)
		self._from(model)

	def _from(self, model):
		for field in model._meta:
			table, col = field.split(".")
			self.fields.append(f"{field} as {table}_{col}")
		self.fields.append(f"{table}.id as {table}_id")

		return self

	def leftjoin(self, model):
		self._from(model)
		table = camelsnake.camel_to_snake(model.__name__)
		self.joins.append(f" LEFT JOIN {table} ON {table}.id = {self.aggr}.{table}_id")

		return self

	def whereId(self, condition):
		self.predicates.append(f" WHERE {self.aggr}.id = ?")

		return self

	def where(self, aggr_field, other_field="?"):
		self.predicates.append(f" WHERE {self.aggr}.{aggr_field} = {other_field}")

		return self

	def __str__(self):
		sql = "SELECT "+", ".join(self.fields)
		sql += f" FROM {self.aggr}"
		if len(self.joins) > 0:
			sql += f" ".join(self.joins)

		if len(self.predicates) > 0:
			sql += " ".join(self.predicates)

		return sql