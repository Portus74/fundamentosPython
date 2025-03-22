from minhasFuncoes import *

# Exemplos de uso das funções
def main():
    # Teste 5: Remoção de duplicados
    print("\n=== Teste de Remoção de Duplicados ===")
    lista_com_duplicados = [1, 2, 2, 3, 3, 4, 5, 5]
    print(f"Lista original: {lista_com_duplicados}")
    print(f"Lista sem duplicados: {remove_duplicados(lista_com_duplicados)}")


if __name__ == "__main__":
    main()