from random import randint

class Die:
  """一つのサイコロを転がすクラス"""
  def __init__(self,num_sides=6):
    """六面のサイコロを初期化する"""
    self.num_sides = num_sides

  def roll(self):
    """1から面の数の間のランダムな数字を返す"""
    return randint(1,self.num_sides)