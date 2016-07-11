n = input()
l = []
# Using underscore ("_") as the variable name in the for appears to be common practice when you don't intend to use the variable in the loop. Underscore is a valid variable name, so you could use it in the loop, but it would make for unreadable code (what does underscore mean?) so using it designates that the variable has no meaning or is otherwise unnecessary.
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        print cmd

        eval("l."+cmd)
        print l
    else:
        print l
