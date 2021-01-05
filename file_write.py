def main():
  f_name = input("Enter your file name : ")
  desp = input("Enter your description : ")

  f = open(f_name, "w", encoding="utf8")
  f.writelines(desp)
  f.close()

if __name__ == '__main__':
  main()
