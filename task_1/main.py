def total_salary(path: str) -> tuple[int, int]:
  """
  Analyzes this file by `path` and returns the total and average salaries of all developers.

  Parameters:
     path (str): path to a text file

  Returns:
    tuple ([int, int]): A tuple containing two integers:
      - `total` salary; `0` if any error occurs
      - `average` salary; `0` if any error occurs
  """

  try:
    with open(path, "r", encoding="utf-8") as file:
      salaries = []
      for dev_info in file.readlines():
        dev_info = dev_info.strip()
        if not dev_info:
          continue

        _, salary = dev_info.split(",")
        salaries.append(int(salary))

      total = sum(salaries)
      average = round(total/len(salaries))
      return (total, average)

  except FileNotFoundError:
    print("The file is missing.")
    return (0, 0)

  except ValueError:
    print("The file has incorrect data.")
    return (0, 0)

  except ZeroDivisionError:
    print("The file has no data.")
    return (0, 0)


if __name__ == "__main__":
  def check_helper(path: str) -> None:
    total, average = total_salary(path)
    print(f"Total salary: {total}, average salary: {average}.")

  check_helper("task_1/documents/salary_file.txt") # Total salary: 6000, average salary: 2000.
  check_helper("task_1/documents/salary_file_empty.txt") # The file has no data. /n Total salary: 0, average salary: 0.
  check_helper("task_1/documents/salary_file_with_errors.txt") # The file has incorrect data. Total salary: 0, average salary: 0.
  check_helper("task_1/documents/salary_file_non_existing.txt") # The file is missing. /n Total salary: 0, average salary: 0.