import java.util.*;

public class Pacman {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int startX = sc.nextInt(), startY = sc.nextInt();
        int goalX = sc.nextInt(), goalY = sc.nextInt();
        int n = sc.nextInt(), m = sc.nextInt();
        sc.nextLine();
        char[][] map = new char[n][m];
        for (int i = 0; i < n; i++) {
            String tmp = sc.nextLine();
            for (int j = 0; j < m; j++)
                map[i][j] = tmp.charAt(j);
        }

        Game game = new Game(goalX, goalY, startX, startY, new int[]{n, m}, map);
        game.printOptimalPath();
    }
}

class Game {
    MapPoint goal;
    MapPoint start;
    int[] mapSize;
    char[][] map;
    HashSet<String> visit;

    Game(int goalX, int goalY, int startX, int startY, int[] mapSize, char[][] map) {
        goal = new MapPoint(goalX, goalY);
        start = new MapPoint(startX, startY);
        this.mapSize = mapSize;
        this.map = map;
    }

    void printOptimalPath() {
        PriorityQueue<TreeNode> leaves = new PriorityQueue<>(new TreeNodeComparator());
        visit = new HashSet<>();
        leaves.add(new TreeNode(start, null, 0, MapPoint.manhattanDist(start, goal), null));
        visit.add(pointHashKey(start));

        while (true) {
            TreeNode node = leaves.poll();
            if (node.point.x == goal.x && node.point.y == goal.y) {
                node.printPath();

                return;
            }

            addPossibleNeighbors(node, leaves, visit);
        }
    }

    private void addPossibleNeighbors(TreeNode node, PriorityQueue<TreeNode> heap, HashSet<String> visit) {
        List<Move> neighbors = node.point.getNeighbors(mapSize[0], mapSize[1]);
        for (Move neighbor: neighbors) {
            if (map[neighbor.point.x][neighbor.point.y] != '%' && !visit.contains(pointHashKey(neighbor.point))) {
                heap.add(new TreeNode(neighbor.point, node, node.g + 1, MapPoint.manhattanDist(neighbor.point, goal), neighbor.movement));
                visit.add(pointHashKey(neighbor.point));
            }
        }
    }

    private String pointHashKey(MapPoint p) {
        return p.x + "," + p.y;
    }
}

class TreeNode {
    MapPoint point;
    TreeNode parent;
    int g;
    int h;

    Move.Movement prevMove;

    TreeNode(MapPoint point, TreeNode parent, int g, int h, Move.Movement prevMove) {
        this.point = point;
        this.parent = parent;
        this.g = g;
        this . h = h;
        this.prevMove = prevMove;
    }

    int f() {
        return g + h;
    }

    void printPath() {
        if (parent != null)
            parent.printPath();

        System.out.println(point.x + " " + point.y);
    }
}

class TreeNodeComparator implements Comparator<TreeNode> {
    @Override
    public int compare(TreeNode o1, TreeNode o2) {
        if (o1.f() != o2.f())
            return o1.f() - o2.f();

        return o1.prevMove.ordinal() - o2.prevMove.ordinal();
    }
}

class MapPoint {
    int x;
    int y;

    MapPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    static int manhattanDist(MapPoint p1, MapPoint p2) {
        return Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y);
    }

    List<Move> getNeighbors(int maxX, int maxY) {
        List<Move> result = new ArrayList<>();
        if (x != 0)
            result.add(new Move(new MapPoint(x-1, y), Move.Movement.U));
        if (y != 0)
            result.add(new Move(new MapPoint(x, y-1), Move.Movement.L));
        if (x != maxX-1)
            result.add(new Move(new MapPoint(x+1, y), Move.Movement.D));
        if (y != maxY-1)
            result.add(new Move(new MapPoint(x, y+1), Move.Movement.R));

        return result;
    }
}

class Move {
    enum Movement {
        U,
        L,
        R,
        D,
    }

    MapPoint point;
    Movement movement;

    Move(MapPoint point, Movement movement) {
        this.point = point;
        this.movement = movement;
    }
}