#Problem 10
def seive(n):
  items = list(xrange(2, n + 1))
  largest = 1
  prime_count = 0
  sm = 0
  for x in items:
    if x == 0:
      continue
    # print x
    mult = 2
    while x * mult <= n:
      items[(x * mult) - 2] = 0
      mult += 1
  return sum(items)
print seive(2000000)

#Problem 9
for x in xrange(1, 1000):
  for y in xrange(1, 1000):
    z = ((x ** 2 + y ** 2) ** 0.5)
    if z % 1 != 0:
      continue
    if x + y + z == 1000:
      print x*y*z

#Problem 8
nm_str = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
mx = 0
for x in xrange( 0, len(nm_str) - 13):
  as_ints = [int(x) for x in nm_str[x:x+13]]
  prod = 1
  for y in as_ints:
    prod *= y
  mx = max(mx, prod)
print mx
# Problem 7
def seive(n):
  items = list(xrange(2, n + 1))
  largest = 1
  prime_count = 0
  for x in items:
    if x == -1:
      continue
    # print x
    prime_count += 1
    print prime_count
    if prime_count == 10001:
      print "Prime! %s" % x
      return x
    mult = 2
    while x * mult <= n:
      items[(x * mult) - 2] = -1
      mult += 1
print seive(20000000)

#Problem 6
natural_nums = list(xrange(1, 101))
sm = sum(natural_nums)
sqrs = [x ** 2 for x in natural_nums]
sqr_sum = sum(sqrs)
sum_sqr = sm ** 2
print sum_sqr - sqr_sum

#Problem 5
divs = [20,19,18,17,16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
for i in xrange(1, 1000000000):
  done = True
  for j in divs:
    if i % j != 0:
      done = False
      break
  if done:
    print i
    break


#Problem 4:
def palindromes():
  largest = 0
  for i in xrange(100, 1000):
    for j in xrange(100, 1000):
      nmbr = i * j
      as_string = "%s" % nmbr
      is_palindrome = as_string == as_string[::-1]
      if is_palindrome and nmbr > largest:
        largest = nmbr
  return largest

print palindromes()

#Problem 3
def seive(n):
  items = list(xrange(2, n + 1))
  largest = 1
  for x in items:
    if x == -1:
      continue
    # print x
    mult = 2
    while x * mult <= n:
      items[(x * mult) - 2] = -1
      mult += 1
    if 600851475143 % x == 0:
      largest = x
  print largest
seive(775147)

#Problem 2
def fib():
  last, current = 1, 2
  sm = 0
  while current <= 4000000:
    sm = sm + current if current % 2 == 0 else sm
    last, current = current, last + current
  print sm

fib()

# Problem 1
sm = 0
for i in xrange(0, 1000):
  sm = sm + i if i % 3 == 0 or i % 5 == 0 else sm
print sm