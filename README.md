=== Setup ===

<ol>
<li>
go to your codes directory
</li>

<li>
`cd ..`
</li>

<li>
`git clone https://github.com/dwihdyn/lifeskill-be.git`
</li>

<li>
ignore this step if you create an environment already. else, go to terminal and run

<ul>
  <li>`conda create -n lifeskill-be python=3.7`</li>
  <li>`source activate lifeskill-be`</li>
</ul>
</li>

<li>
move your codes to under 'lifeskill_web' directory
</li>

<li>
run below code in terminal

<ul>
  <li>`pip install -r requirements.txt`</li>
  <li>`pip freeze > requirements.txt`</li>
</ul>
</li>

<li>
branch out
`git checkout -b whateverFeatureYouAreBuilding`
</li>

<li>
put your codes accordingly to the boilerplate, make sure it works as usual
</li>

<li>
once working, continue build your feature
</li>

<li>
publish your codes into github

<ul>
  <li>`cd ..`</li>
  <li>`git add .`</li>
  <li>`git commit -m 'my feature - yourName'`</li>
  <li>`git push origin whateverFeatureYouAreBuilding`</li>
</ul>
</li>

<li> (IMPORTANT !!!!!!!!!!!) :
MAKE SURE you are in the right branch
`git branch`
if it show "whateverFeatureYouAreBuilding" in green color, you on the right track
</li>
</ol>
if you stuck, let dwi know on slack

Remember to build one feature at a time! and good luck :)

=================================================================================

Some git command you can explore:

<ul>
  <li>`git branch` : see all available branches</li>
  <li>`git checkout branch-name` : change branch to branch-name </li>
  <li>`git fetch origin other-people-branch` : to put other people (in progress) code into your local computer</li>
</ul>
