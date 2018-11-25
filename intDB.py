from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Categories, Base, CatalogItem, User

engine = create_engine('sqlite:///ItemCatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Mohammed", email="moh@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
Category1 = Categories(user_id=1, name="Sport")
session.add(Category1)
session.commit()

Category2 = Categories(user_id=1, name="Fantasy")
session.add(Category2)
session.commit()

Category3 = Categories(user_id=1, name="Horror")
session.add(Category3)
session.commit()


CatalogItem1 = CatalogItem(user_id=1, name="FIFA 19", description="delivers a champion-caliber experience on and off the pitch. Led by the prestigious UEFA Champions League, FIFA 19 offers enhanced gameplay features that allow you to control the pitch in every moment",
                           imageUrl="https://pbs.twimg.com/media/DfRYq74V4AAqmTg.jpg", price="59.9$", categories=Category1)
session.add(CatalogItem1)
session.commit()

CatalogItem2 = CatalogItem(user_id=1, name="PES 19", description="PES 2019 is a sports game that simulates football. PES 2019's Magic Moments feature is set to be the forefront of its superior gameplay.",
                           imageUrl="https://images.performgroup.com/di/library/GOAL/eb/6b/embed-only-pes-2019-cover_1pft6v9plo5cz1g994k1okwegj.png?t=425955981", price="69.9$", categories=Category1)
session.add(CatalogItem2)
session.commit()

CatalogItem3 = CatalogItem(user_id=1, name="Uncharted 4", description="A Thief’s End raises the bar on video games and is the best overall fantasy game due to its breathtaking graphics, dynamic storytelling, professional orchestra and exciting gameplay.",
                           imageUrl="https://www.lifewire.com/thmb/xYBqAZSsKPUyDC1y9Yu14n_wZak=/640x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Uncharted41-5b22d0a2a9d4f90037236a58.jpg", price="59.9$", categories=Category2)
session.add(CatalogItem3)
session.commit()


print ("added menu items!")
