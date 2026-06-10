from model.car_configuration import Car_Configuration
from model.quote import Quote, QuoteItem
from repository import car_configuration_repository
from model import engine,optional,accessories


#  ── CONFIGURATION SERVICE 

#  aggiungi_componente → aggiunge un componente alla Quote (preventivo) 
#  configurazione FINALE → trasforma la Quote in Car_Configuration



#         quote          → la Quote a cui aggiungere il componente
#         component_type → 'accessory', 'optional' o 'engine'
#         component_id   → id del componente nella sua tabella
#         price          → prezzo attuale del componente (diventa price_snapshot)
def add_component(session,Quote,component_type,component_id):



    valid_component=[engine,optional,accessories]
    if component_type not in valid_component:
        raise ValueError (f"il componente non è valido, usa uno dei seguenti{valid_component}")
    

    already_existing_componentany= any( item.component_type == component_type and item.component_id== component_id for item in Quote.items)
    if  already_existing_componentany:
        raise ValueError(f'Il componente {component_type} #{component_id} è stato già selezionato ')
    


    new_item=()
    



    
