import matplotlib.pyplot as plt
import matplotlib.axes as ax

plt.gcf().subplots_adjust(bottom=0.25)
plt.title("Accuracy Comparison")

plt.tick_params(axis='x',labelbottom=False,direction="in")

plt.ylabel("Accuracy(%)")
plt.ylim(0,100)
plt.xlim(0,6000)
plt.plot([1426,3324,3604,4933,5644], [47.16,46.15,67.5,68,70], 'b', label='line 1', linewidth=1)
plt.plot([1426,3324,3604,4933,5644], [58.19,59.87,73,76.5,78], 'g', label='line 1', linewidth=1)
plt.plot([1426,3324,3604,4933,5644], [67.89,59.87,58,69,74.5], 'r', label='line 1', linewidth=1)
plt.plot([3604,4933,5644], [65.5,73,77.5], 'y', label='line 1', linewidth=1)

plt.plot([1426,3324,3604,4933,5644], [47.16,46.15,67.5,68,70], 'g.', label='line 1', linewidth=1)
plt.plot([1426,3324,3604,4933,5644], [58.19,59.87,73,76.5,78], 'bo', label='line 1', linewidth=1)
plt.plot([1426,3324,3604,4933,5644], [67.89,59.87,58,69,74.5], 'y^', label='line 1', linewidth=1)
plt.plot([3604,4933,5644], [65.5,73,77.5], 'rp', label='line 1', linewidth=1)



columns = (1426,3324,3604,4933,5644)
rows = ["MNB","Linear SVC","RBF SVC","CNN LSTM"]

cell_text=[]
cell_text.append([47.16,46.15,67.5,68,70])
cell_text.append([58.19,59.87,73,76.5,78])
cell_text.append([67.89,59.87,58,69,74.5])
cell_text.append(['n/a','n/a',65.5,73,77.5])

the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      colLabels=columns,
                      loc='bottom')



plt.show()
