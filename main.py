from service import executar, listar_categorias, listar_programas


categoria = listar_categorias()
programa = listar_programas(categoria)
executar(programa, categoria)