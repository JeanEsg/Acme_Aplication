#Clase repositorio tiene comunicación directa con la base de datos
from configurations import db
from Model.FormularioModel import FormularioModel
from bson import ObjectId
class FormularioRepository:
    
    #Metodo constructor de clase e instanciando la base de datos
    def __init__(self):
        self.collection = db['Formulario']

    #Insertar un formulario en la base de datos
    def crear_formulario(self, formulario:FormularioModel):
        form_data = formulario.dict(by_alias=True)
        result = self.collection.insert_one(form_data)
        return str(result.inserted_id)

    #Trae los formularios creados en la base de datos
    def listar_formularios(self):
        return [FormularioModel(**{**doc, "_id": str(doc["_id"])}) for doc in self.collection.find()]

    #Trae un formulario segun la norma
    def listar_formulario_por_nombre(self, nombre: str):
        data = self.collection.find_one({"nombre": nombre})
        if data:
            data["_id"] = str(data["_id"])
            return FormularioModel(**data)
        return None
    
    #Elimina un formulario de la base de datos por su id
    def eliminar_formulario_por_id(self, id: str) -> bool:
        result = self.collection.delete_one({"_id": id})
        return result.deleted_count > 0

   
