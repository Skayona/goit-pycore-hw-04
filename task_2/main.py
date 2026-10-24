def get_cats_info(path: str) -> list[dict]:
  """
  Returns a list of dictionaries containing information about each cat.

  Parameters:
     path (str): path to a text file

  Returns:
    list (dict): A list of dictionaries, where each dictionary contains information about one cat.
      - name
      - id
      - age
  """

  try:
    with open(path, "r", encoding="utf-8") as file:
      cats_data_base = []
      for cat_info in file.readlines():
        cat_info = cat_info.strip()
        if not cat_info:
          continue

        id, name, age = cat_info.split(",")
        cats_data_base.append({
          "id": id,
          "name": name,
          "age": age
        })

      return cats_data_base

  except FileNotFoundError:
    print("The file is missing.")
    return []

  except ValueError:
    print("The file has incorrect data.")
    return []


if __name__ == "__main__":
  def check_helper(path: str) -> None:
    print(get_cats_info(path))

  # [
  #   {'id': '60b90c1c13067a15887e1ae1', 'name': 'Tayson', 'age': '3'},
  #   {'id': '60b90c2413067a15887e1ae2', 'name': 'Vika', 'age': '1'},
  #   {'id': '60b90c2e13067a15887e1ae3', 'name': 'Barsik', 'age': '2'},
  #   {'id': '60b90c3b13067a15887e1ae4', 'name': 'Simon', 'age': '12'},
  #   {'id': '60b90c4613067a15887e1ae5', 'name': 'Tessi', 'age': '5'}
  # ]
  check_helper("task_2/cats_data_base/cats_data_base.txt")
  check_helper("task_2/cats_data_base/cats_data_base_empty.txt") # []
  check_helper("task_2/cats_data_base/cats_data_base_missing_data.txt") # The file has incorrect data. []
  check_helper("task_2/cats_data_base/cats_data_base_non_existing.txt") # The file is missing. []
