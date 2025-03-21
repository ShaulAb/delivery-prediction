import pandas as pd

categories_mapping = [
    ['perfumaria', 'perfumery'],
    ['artes', 'arts'],
    ['esporte_lazer', 'sports_leisure'],
    ['bebes', 'babies'],
    ['utilidades_domesticas', 'household_utilities'],
    ['instrumentos_musicais', 'musical_instruments'],
    ['cool_stuff', 'cool_stuff'],
    ['moveis_decoracao', 'furniture_decoration'],
    ['eletrodomesticos', 'home_appliances'],
    ['brinquedos', 'toys'],
    ['cama_mesa_banho', 'bed_table_bath'],
    ['construcao_ferramentas_seguranca', 'construction_tools_safety'],
    ['informatica_acessorios', 'computing_accessories'],
    ['beleza_saude', 'beauty_health'],
    ['malas_acessorios', 'bags_accessories'],
    ['ferramentas_jardim', 'garden_tools'],
    ['moveis_escritorio', 'office_furniture'],
    ['automotivo', 'automotive'],
    ['eletronicos', 'electronics'],
    ['fashion_calcados', 'fashion_footwear'],
    ['telefonia', 'telephony'],
    ['papelaria', 'stationery'],
    ['fashion_bolsas_e_acessorios', 'fashion_bags_and_accessories'],
    ['pcs', 'pcs'],
    ['casa_construcao', 'house_construction'],
    ['relogios_presentes', 'watches_gifts'],
    ['construcao_ferramentas_construcao', 'construction_tools_construction'],
    ['pet_shop', 'pet_shop'],
    ['eletroportateis', 'portable_electronics'],
    ['agro_industria_e_comercio', 'agro_industry_and_trade'],
    [None, None],
    ['moveis_sala', 'living_room_furniture'],
    ['sinalizacao_e_seguranca', 'signaling_and_safety'],
    ['climatizacao', 'climate_control'],
    ['consoles_games', 'consoles_games'],
    ['livros_interesse_geral', 'general_interest_books'],
    ['construcao_ferramentas_ferramentas', 'construction_tools_tools'],
    ['fashion_underwear_e_moda_praia', 'fashion_underwear_and_beachwear'],
    ['fashion_roupa_masculina', 'fashion_mens_clothing'],
    ['moveis_cozinha_area_de_servico_jantar_e_jardim', 'kitchen_service_dining_and_garden_furniture'],
    ['industria_comercio_e_negocios', 'industry_trade_and_business'],
    ['telefonia_fixa', 'fixed_telephony'],
    ['construcao_ferramentas_iluminacao', 'construction_tools_lighting'],
    ['livros_tecnicos', 'technical_books'],
    ['eletrodomesticos_2', 'home_appliances_2'],
    ['artigos_de_festas', 'party_supplies'],
    ['bebidas', 'drinks'],
    ['market_place', 'marketplace'],
    ['la_cuisine', 'the_kitchen'],
    ['construcao_ferramentas_jardim', 'construction_tools_garden'],
    ['fashion_roupa_feminina', 'fashion_womens_clothing'],
    ['casa_conforto', 'home_comfort'],
    ['audio', 'audio'],
    ['alimentos_bebidas', 'food_drinks'],
    ['musica', 'music'],
    ['alimentos', 'food'],
    ['tablets_impressao_imagem', 'tablets_printing_imaging'],
    ['livros_importados', 'imported_books'],
    ['portateis_casa_forno_e_cafe', 'portable_house_oven_and_coffee'],
    ['fashion_esporte', 'fashion_sports'],
    ['artigos_de_natal', 'christmas_supplies'],
    ['fashion_roupa_infanto_juvenil', 'fashion_children_teen_clothing'],
    ['dvds_blu_ray', 'dvds_blu_ray'],
    ['artes_e_artesanato', 'arts_and_crafts'],
    ['pc_gamer', 'pc_gamer'],
    ['moveis_quarto', 'bedroom_furniture'],
    ['cine_foto', 'cinema_photography'],
    ['fraldas_higiene', 'diapers_hygiene'],
    ['flores', 'flowers'],
    ['casa_conforto_2', 'home_comfort_2'],
    ['portateis_cozinha_e_preparadores_de_alimentos', 'portable_kitchen_and_food_preparators'],
    ['seguros_e_servicos', 'insurance_and_services'],
    ['moveis_colchao_e_estofado', 'mattress_and_upholstery_furniture'],
    ['cds_dvds_musicais', 'musical_cds_dvds']
]

categories_translations = pd.DataFrame(categories_mapping, columns=['product_category_name', 'product_category'])


special_characters = {
    'ã': 'a',
    'á': 'a',
    'â': 'a',
    'à': 'a',
    'ç': 'c',
    'é': 'e',
    'ê': 'e',
    'í': 'i',
    'ó': 'o',
    'ô': 'o',
    'ú': 'u',
    'ñ': 'n',
    'ü': 'u',
    'õ': 'o',
    'ß': 'ss',
    'Á': 'A',
    'À': 'A',
    'Â': 'A',
    'Ã': 'A',
    'É': 'E',
    'Ê': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ô': 'O',
    'Ú': 'U',
}

city_coords_df = pd.read_csv('../data/city_coords.csv')
