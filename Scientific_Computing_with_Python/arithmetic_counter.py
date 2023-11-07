def arithmetic_arranger(exp_list, res= False):
    arranged_problems=""
    l_op=[]
    r_op=[]
    oper=[]
    reslst=[]
    top_line = ""
    middle_line = ""
    bottom_line = ""
    if len(exp_list) > 5:
      return "Error: Too many problems."
    for exp in exp_list:
      if '*' in exp or '/' in exp:
        return "Error: Operator must be '+' or '-'."
      comp= exp.split()
      left_op, op, right_op= comp[0], comp[1], comp[2]
      l_op.append(left_op)
      r_op.append(right_op)
      oper.append(op)
      if not left_op.isdigit() or not right_op.isdigit():
        return "Error: Numbers must only contain digits."
      if len(left_op) > 4 or len(right_op) > 4:
        return "Error: Numbers cannot be more than four digits."
      if res:
        if op == '+':
          sum = int(left_op) + int(right_op)
          reslst.append(sum)
        if op == '-':
          diff = int(left_op) - int(right_op)
          reslst.append(diff)
    for i in range(len(l_op)):
      number_str = str(l_op[i])
      rnumber_str = str(r_op[i])
      operator_str = oper[i]
      max_ele=max(int(l_op[i]), int(r_op[i]))
      if int(l_op[i]) == max_ele:
        width= len(l_op[i])+2
      else:
        width= len(r_op[i])+2
      if i == len(l_op)-1:
        top_line += number_str.rjust(width)
        middle_line += operator_str + " " + rnumber_str.rjust(width - 2)
        bottom_line += "-" * width
      else:  
        top_line += number_str.rjust(width) + "    "
        middle_line += operator_str + " " + rnumber_str.rjust(width - 2) + "    "
        bottom_line += "-" * width + "    "
      arranged_problems = top_line  + "\n" + middle_line + "\n" + bottom_line
      if res:
        arranged_problems += "\n"
      for i in range(len(reslst)):
        if i == len(reslst)-1:
          arranged_problems += str(reslst[i]).rjust(max(len(l_op[i]), len(r_op[i])) + 2)
        else:
          arranged_problems += str(reslst[i]).rjust(max(len(l_op[i]), len(r_op[i])) + 2) + "    "
    return arranged_problems