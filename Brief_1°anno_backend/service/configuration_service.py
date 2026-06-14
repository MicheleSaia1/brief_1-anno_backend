from model.car_configuration import Car_Configuration
from model.quote import Quote, QuoteItem
from repository import car_configuration_repository
from model import engine,optional,accessories


#  ── CONFIGURATION SERVICE 

#  aggiungi_componente → aggiunge un componente alla Quote (preventivo) 
#  configurazione FINALE → trasforma la Quote in Car_Configuration



def add_component(session,quote,component_type,component_id):

    if quote.is_finalized:
        raise ValueError("La Quote è già finalizzata, non modificabile")



    valid_component=[engine,optional,accessories]
    if component_type not in valid_component:
        raise ValueError (f"il componente non è valido, usa uno dei seguenti{valid_component}")
    
# 
    already_existing_componentany= any( item.component_type == component_type and item.component_id == component_id for item in Quote.items)
    if  already_existing_componentany:
        raise ValueError(f'component {component_type} #{component_id} already selected ')
    

    #prezzo attuale del preventivo 
    price_configuration = QuoteItem(
    quote_id=Quote.id,
    component_type=component_type,
    component_id=component_id,
    )

    QuoteItem.append(price_configuration)
    session.commit()

    
    
    
    
    
    
    component_remove = next(
        (item for item in quote.items
        if item.component_type == component_type and item.component_id==component_id),
    None
    )


    
    
    
    
    
    
    if quote.is_finalized:
        raise ValueError("Già finalizzata")

    if not quote.items:
        raise ValueError("no items selected")

    
    #car configuration
    config = Car_Configuration(
    user_id=quote.user_id,
    car_id=quote.car_id,
    total_price=quote.total,  # congela il totale
    quote=quote
    )
    return car_configuration_repository.create(session, config)





# # def finalizza_configurazione(session, quote: Quote) -> Car_Configuration:
# #     """
# #     Trasforma una Quote in una Car_Configuration permanente.

# #     Parametri:
# #         session → sessione DB
# #         quote   → la Quote da finalizzare (deve avere almeno un componente)

# #     Ritorna:
# #         La Car_Configuration appena creata.
# #     """

# #     if quote.is_finalized:
# #         raise ValueError(f"La Quote #{quote.id} è già stata finalizzata")

# #     if not quote.items:
# #         raise ValueError("Non puoi finalizzare una Quote senza componenti selezionati")

# #     # Creiamo la configurazione.
# #     # quote.total è la @property di Quote: prezzo base auto + tutti i price_snapshot
# #     # Lo salviamo come numero fisso: da questo momento il totale non cambierà mai
# #     config = Car_Configuration(
# #         user_id=quote.user_id,
# #         car_id=quote.car_id,
# #         total_price=quote.total,
# #         quote=quote              # SQLAlchemy imposta automaticamente quote_id
# #     )

# #     return car_configuration_repository.create(session, config)
    
    



    
