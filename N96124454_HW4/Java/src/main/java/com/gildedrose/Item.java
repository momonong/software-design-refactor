public class Item {
    protected String name;
    protected int sellIn;
    protected int quality;
    protected UpdateQuality updater;

    public Item(String name, int sellIn, int quality) {
        this.name = name;
        this.sellIn = sellIn;
        this.quality = quality;
    }

    public void update() {
        updater.update(this);
    }
}

public class AgedBrie extends Item {

    public AgedBrie(int sellIn, int quality) {
        super("Aged Brie", sellIn, quality);
        this.updater = new AgedBrieUpdate();
    }
}

public class Sulfuras extends Item {

    public Sulfuras(int sellIn, int quality) {
        super("Sulfuras, Hand of Ragnaros", sellIn, quality);
        this.updater = new SulfurasUpdate();
    }
}

public class BackstagePasses extends Item {

    public BackstagePasses(int sellIn, int quality) {
        super("Backstage passes to a TAFKAL80ETC concert", sellIn, quality);
        this.updater = new BackstagePassesUpdate();
    }
}

public class ConjuredItem extends Item {

    public ConjuredItem(String name, int sellIn, int quality) {
        super(name, sellIn, quality);
        this.updater = new ConjuredUpdate();
    }
}
