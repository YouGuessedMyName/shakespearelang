s = """
"'Achilles' 'Adonis' 'Adriana' 'Aegeon'"
"'Aemilia' 'Agamemnon' 'Agrippa' 'Ajax'"
"'Alonso' 'Andromache' 'Angelo'"
"'Antiochus' 'Antonio' 'Arthur'"
"'Autolycus' 'Balthazar' 'Banquo'"
"'Beatrice' 'Benedick' 'Benvolio'"
"'Bianca' 'Brabantio' 'Brutus' 'Capulet'"
"'Cassandra' 'Cassius' 'Christopher'"
"'Cicero' 'Claudio' 'Claudius'"
"'Cleopatra' 'Cordelia' 'Cornelius'"
"'Cressida' 'Cymberline' 'Demetrius'"
"'Desdemona' 'Dionyza' 'Doctor'"
"'Dogberry' 'Don' 'Donalbain' 'Dorcas'"
"'Duncan' 'Egeus' 'Emilia' 'Escalus'"
"'Falstaff' 'Fenton' 'Ferdinand' 'Ford'"
"'Fortinbras' 'Francisca' 'Friar'"
"'Gertrude' 'Goneril' 'Hamlet' 'Hecate'"
"'Hector' 'Helen' 'Helena' 'Hermia'"
"'Hermonie' 'Hippolyta' 'Horatio'"
"'Imogen' 'Isabella' 'John' 'Julia'"
"'Juliet' 'Julius' 'King' 'Lady' 'Lennox'"
"'Leonato' 'Luciana' 'Lucio' 'Lychorida'"
"'Lysander' 'Macbeth' 'Macduff' 'Malcolm'"
"'Mariana' 'Mark' 'Mercutio' 'Miranda'"
"'Mistress' 'Montague' 'Mopsa' 'Oberon'"
"'Octavia' 'Octavius' 'Olivia' 'Ophelia'"
"'Orlando' 'Orsino' 'Othello' 'Page'"
"'Pantino' 'Paris' 'Pericles' 'Pinch'"
"'Polonius' 'Pompeius' 'Portia' 'Priam'"
"'Prince' 'Prospero' 'Proteus' 'Publius'"
"'Puck' 'Queen' 'Regan' 'Robin' 'Romeo'"
"'Rosalind' 'Sebastian' 'Shallow'"
"'Shylock' 'Slender' 'Solinus' 'Stephano'"
"'Thaisa' 'The' 'Theseus' 'Thurio'"
"'Timon' 'Titania' 'Titus' 'Troilus'"
"'Tybalt' 'Ulysses' 'Valentine' 'Venus'"
"'Vincentio' 'Viola'"
"""
print(s.replace("' '", " | ").replace(""""'""", "").replace("""'"\n""", " | "))