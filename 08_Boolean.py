# What is Boolean 
# 👉 Boolean एउटा data type हो जसले दुई मानमात्र (True वा False) राख्छ।
#यसलाई हामी साँचो (True) र झूटो (False) को रूपमा बुझ्न सक्छौं।


#  Boolean किन प्रयोग गरिन्छ?
#👉 Boolean धेरै ठाउँमा काम लाग्छ, खासगरी logic निर्णयहरू, if statement, comparison मा।

# Boolean मानहरू Python मा:

a = True
b = False

print(a)  # Output: True
print(b)  # Output: False


#  Boolean कसरी बनाइन्छ?
#Comparison operators (जस्तै: ==, !=, >, <, >=, <=) प्रयोग गरेर Boolean मान निकाल्न सकिन्छ।

x = 10
y = 20

print(x > y)    # False, किनकि 10 > 20 होइन
print(x < y)    # True, किनकि 10 < 20 हो
print(x == 10)  # True, किनकि x बराबर 10 हो
print(y != 20)  # False, किनकि y बराबर 20 हो



# Boolean Logical Operators:
#   Operator	 Meaning	  Example	         Result
#   and	           र	     True and False	     False
#   or	           वा	     True or False	     True
#   not	           होइन	     not True	         False


# Example 
# a = True
# b = False

# print(a and b)   # False
# print(a or b)    # True
# print(not a)     # False


# Boolean सँग if statement:

is_raining = True

if is_raining:
    print("छाता लिएर जानुस्")
else:
    print("छाता नलिए पनि हुन्छ")


# Short Summary 

# Boolean को मान दुई हुन्छ: True वा False

#Comparison गर्न Boolean प्रयोग हुन्छ (जस्तै: ==, <, >)

#Logical operation गर्न Boolean operators (and, or, not) प्रयोग हुन्छ।


