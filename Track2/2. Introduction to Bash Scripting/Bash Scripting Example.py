
"""
Bash Scripting Example 

note ~ this would need to be run in a terminal, not actual python scripts
"""


"""
Example 1  - Basic scripting example, creating an array 
"""
# Create variables from the temperature data files
temp_b="$(cat temps/region_B)"
temp_c="$(cat temps/region_C)"

# Create an array with these variables as elements
region_temps=($temp_b $temp_c)

# Call an external program to get average temperature
average_temp=$(echo "scale=2; (${region_temps[0]} + ${region_temps[1]}) / 2" | bc)

# Append average temp to the array
region_temps+=($average_temp)

# Print out the whole array
echo ${region_temps[@]}


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------

"""
Example 2 - If statements 
"""
# Extract Accuracy from first ARGV element
accuracy=$(grep "Accuracy" $1 | sed 's/.* //')

# Conditionally move into good_models folder
if [ $accuracy -ge 90 ]; then
    mv $1 good_models/
fi

# Conditionally move into bad_models folder
if [ $accuracy -lt 90 ]; then
    mv $1 bad_models/
fi

# Then in terminal can run:
# bash script.sh model_results/model_1.txt     - which is bash, script name, followed by any arguments (in order!)

#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
"""
Example 3 - If statements 
"""
# Create variable from first ARGV element
sfile=$1

# Create an IF statement on first ARGV element's contents
if grep -q 'SRVM_' $sfile && grep -q 'vpt' $sfile ; then
	# Move file if matched
	mv $sfile good_logs/
fi

>> to then run:     bash script.sh myfiles/logfiles8.txt     for example

#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
"""
Example 4 - For Looping 
"""
# Use a FOR loop on files in directory
for file in inherited_folder/*.R
do 
    # Echo out each file
    echo $file
done


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
"""
Example 5 - case when 
"""

# Create a CASE statement matching the first ARGV element
case $1 in
  # Match on all weekdays
  Monday|Tuesday|Wednesday|Thursday|Friday)
  echo "It is a Weekday!";;
  # Match on all weekend days
  Saturday|Sunday)
  echo "It is a Weekend!";;
  # Create a default
  *)
  echo "Not a day!";;
esac


bash script.sh Wednesday   >>> will output Its a weekday 


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
"""
Example 6 - Creating a function & then calling it 
"""
# Create function
what_day_is_it () {

  # Parse the results of date
  current_day=$(date | cut -d " " -f1)

  # Echo the result
  echo $current_day
}

# Call the function
what_day_is_it 


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
"""
Example 7 -  Arguments, returning values & scope
"""
# Create a function
function get_number_wins () {

  # Filter aggregate results by argument
  win_stats=$(cat soccer_scores.csv | cut -d "," -f2 | egrep -v 'Winner'| sort | uniq -c | egrep "$1")

}

# Call the function with specified argument
get_number_wins "Etar"

# Print out the global variable
echo "The aggregated stats are: $win_stats"


#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------
"""
Example 8 -  Arguments, returning values & scope

Imagine we have sales figures which are:  14, 12, 23.5, 16 & 19.34   These all total to make 84.84
create a function, that can pass through this array of sales (aka list of numbers) and spit out the total 
"""
# Create a function with a local base variable
function sum_array () {
  local sum=0
  # Loop through, adding to base variable
  for number in "$@"
  do
    sum=$(echo "$sum + $number" | bc)
  done
  # Echo back the result
  echo $sum
  }

# Call function with array
test_array=(14 12 23.5 16 19.34)
total=$(sum_array "${test_array[@]}")
echo "The sum of the test array is $total"


