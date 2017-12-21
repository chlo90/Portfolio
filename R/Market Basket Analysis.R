library(pacman)
#Using pacman to load multiple libraries
pacman::p_load(arules,arulesViz)
data("Groceries")

#Check the the dataset is in transactions type 
str(Groceries)

#Use @ instead of $ if dataset is divided into slots like Data, ItemInfo, itemsetInfo here
head(Groceries@itemInfo)

#create an item frequency plot 
arules::itemFrequencyPlot(Groceries, topN = 20, type='relative', 
                  main = 'Relative Item Frequency Plot', ylab = 'item frequency (relative)')

#Get the rules  - if we want shorter rules (# of linked items), use maxlen = 3 or some number
rules <- apriori(Groceries, parameter = list(supp = 0.001, conf = 0.80))
##########
#Support: basic probability of an event to occur. 
## Support(A) is number of transactions that includes A divided by total number of transactions. 
#Confidence: conditional probability of the occurence; 
##chance of A happening given B already happened. 
#Lift: Tells you how much better a rule is predicting than random guess. ratio of confidence to expected confidence. 
## Probability of all items in rule occuring together (aka support) divided by product of probabilities 
# of the items on the left and right side occuring as if no association between them. 

#Now we see top 10 rules arranged by lift 
inspect(rules[1:10])
# If we buy liquor or red/blush wine, we are very likely to buy bottled beer or 90.5 % likely to buy bottled beer

summary(rules)

#we can sort them by confidence too 
rules_sorted <- sort(rules, by = 'confidence', decreasing = TRUE)
inspect(rules_sorted[1:5])

#Since a lot of people are buying whole milk and other veggies, place eggs beside them to boost sale 

plot(rules[1:20], method='graph', control = list(tpe='items'))
#Gives graph model of how items are associated together 
#size of node based on support, colour on lift ratio, arrow show antecedent

#Parallel coordinates plot 
plot(rules[1:20], method = 'paracoord', control = list(reorder =TRUE))
#matrix representation
plot(rules[1:20], method = 'matrix', control = list(reorder=TRUE))

#if we want to remove redundant rules 
#subset.matrix <- is.subset(rules, rules)
#subset.matrix[lower.tri(subset.matrix, diag=T)] <- NA
#redundant <- colSums(subset.matrix, na.rm = T) >= 1
#rules.pruned <- rules[!redundant]
#rules <- rules.pruned

#Interactive Scatterplot 
plotly_arules(rules)

#Targeting Items (what are customers likely to buy before or after this item)
#What are people buying before they buy whole milk? 
rules <- apriori(data=Groceries, parameter=list(supp=0.001, conf = 0.08), 
                 appearance = list(default = "lhs", rhs = 'whole milk'),
                 control = list(verbose=F))
rules <- sort(rules, decreasing=TRUE, by='confidence')
inspect(rules[1:5])

#What are people buying after they buy whole milk? 
rules <- apriori(data=Groceries, parameter=list(supp=0.001, conf = 0.08), 
                 appearance = list(default = 'rhs', lhs = 'whole milk' ),
                 control = list(verbose=F))
rules <- sort(rules, by = 'confidence', decreasing=TRUE)
inspect(rules[1:5])

#Visualization 
plot(rules, method = 'graph', interactive=TRUE, shading=NA)


#fviz_cluster(sm_kmeans8, data = geom, stand, frame.tpe = 'norm')
clusters_pars = sm_kmeans8$centers
ransposed = t(clusers_pars)
cluster_1 = transposed[[which(abs(transposed[,1]) >= 0.5), 1]
cluster_2 = transposed[which(abs(transposed[,2]) >= 0.5), 2]
