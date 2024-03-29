MAX_DAMAGE = 100.00

DAMAGE_DECORATORS = [
  ['miss', 'misses', 'clumsy', ''],
  ['bruise', 'bruises', 'clumsy', ''],
  ['scrape', 'scrapes', 'wobbly', ''],
  ['scratch', 'scratches', 'wobbly', ''],
  ['lightly wound', 'lightly wounds', 'amateur', ''],
  ['injure', 'injures', 'amateur', ''],
  ['harm', 'harms', 'competent', ', creating a bruise'],
  ['thrash', 'thrashes', 'competent', ', leaving marks'],
  ['decimate', 'decimates', 'cunning', ', the wound bleeds'],
  ['devastate', 'devastates', 'cunning', ', hitting organs'],
  ['mutilate', 'mutilates', 'calculated', ', shredding flesh'],
  ['cripple', 'cripples', 'calculated', ', leaving GAPING holes'],
  ['DISEMBOWEL', 'DISEMBOWELS', 'calm', ', guts spill out'],
  ['DISMEMBER', 'DISMEMBERS', 'calm', ', blood sprays forth'],
  ['ANNIHILATE!', 'ANNIHILATES!', 'furious', ', revealing bones'],
  ['OBLITERATE!', 'OBLITERATES!', 'furious', ', rending organs'],
  ['DESTROY!!', 'DESTROYS!!', 'frenzied', ', shattering bones'],
  ['MASSACRE!!', 'MASSACRES!!', 'barbaric', ', gore splatters everywhere'],
  ['!DECAPITATE!', '!DECAPITATES!', 'deadly', ', scrambling some brains'],
  ['!!SHATTER!!', '!!SHATTERS!!', 'legendary', ' into tiny pieces'],
  ['do UNSPEAKABLE things to', 'does UNSPEAKABLE things to', 'ultimate', '!'],
]

def get_damage_decorator(damage):
  choice_count = len(DAMAGE_DECORATORS)
  damage_percent = damage / MAX_DAMAGE
  choice_index = min(max(int(choice_count * damage_percent), 0), choice_count - 1)
  return DAMAGE_DECORATORS[choice_index]