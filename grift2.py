

ggplot(
   data = data.reset_index(),
   mapping = aes(x = 'Date', y = 'Close')
 ) +\
    geom_line() +\
    ggtitle('Dados históricos do BBAS3.SA') +\
    xlab('Data') +\
    ylab('Fecchamento')


from data.download import download_data