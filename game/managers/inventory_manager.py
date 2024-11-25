from __future__ import annotations

from tcod.ecs import Entity, IsA

from game.components import Name, Position, Quantity
from game.managers.event_manager import Event
from game.tags import IsIn, IsItem


def add_item(actor: Entity, item: Entity) -> None:
    """Add an item to an actor's inventory."""

    # If the actor's inventory already contains an item which is of the same
    # type as the newly added item, add the new item's quantity to the held
    # item's quantity, rather than registering a separate item.
    for held_item in get_items(actor):
        if not can_stack(item, held_item):
            continue
        held_item.components[Quantity] += item.components.get(Quantity)
        Event('inventory_item_added', f"{item.components.get(Name)} x {item.components.get(Quantity)}")
        item.clear()
        return

    # Else, add the new item to the inventory.
    item.components.pop(Position, None)
    item.relation_tag[IsIn] = actor
    Event('inventory_item_added', f"{item.components.get(Name)} x {item.components.get(Quantity)}")


def get_items(actor: Entity):
    """Get all items from an actor's inventory."""

    return actor.registry.Q.all_of(tags=[IsItem], relations=[(IsIn, actor)])


def can_stack(entity: Entity, onto: Entity, /) -> bool:
    """Return True if two entities can be stacked."""

    return bool(
        entity.components.get(Name) == onto.components.get(Name)
        and entity.relation_tag.get(IsA) is onto.relation_tag.get(IsA)
    )
