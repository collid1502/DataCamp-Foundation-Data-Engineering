"""
Text Classification 
"""
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------

"""
Extract, Transform & Select (ETS)
"""

# Importing functions from the pyspark.sql.functions module 
from pyspark.sql.functions import split, explode, length 

# Example of creating our own boolean UDF (User Defined Function)
from pyspark.sql.functions import udf 
from pyspark.sql.types import BooleanType 

short_udf = udf(lambda x:
                    True is not x or len(x) < 10 else False,
                    BooleanType())
    
# we can then use this UDF as we would any built in function 
df.select(short_udf('textdata').alias("is short")).show(3)   # This shows a column 'Is short' and the resulting true or false boolean value for the condition the function passes, for 3 rows

## Important UDF return Types 
from pyspark.sql.types import StringType, IntegerType, FloatType, ArrayType 

#----------------------------------------------------------------------------
# Another example, create a UDF that removes that last word from a list of words {list of words on each row of data} 
from pyspark.sql.types import StringType, ArrayType 

# Removes last item in array 
in_udf = udf(lambda x:
             x[0:len(x)-1] if x and len(x) > 1
             else [],
             ArrayType(StringType())) 

# so, now using the function 
df3.select('word array', in_udf('word array').alias('without endword')).show(5, truncate=30) 
#
# Example Output 
#+----------------------------------------------------------------------------
#|          Word Array   |      without endword                             
#+----------------------------------------------------------------------------
#| ['then','how','many'] |  ['then','how']
#| ['quite','so']        |  ['quite']
#+----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
