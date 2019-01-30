scientists = ['Charles darwin', 'Carl Linnaeus', 'Alfred Wegener', 'Marie Curie', 'Albert Einstein', 'Niels Bohr', 'Isaac Newton', 'Dmitri Mendeleev', 'Antoine Lavoisier']

print (sorted(scientists, key=lambda name: name.split()[-1]))
