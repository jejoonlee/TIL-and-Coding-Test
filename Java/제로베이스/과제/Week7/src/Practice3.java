
class Pager {
    long totalCount;
    long contentPerPage;
    long blocksPerPage;


    public Pager (long totalCount, long contentPerPage, long blocksPerPage) {
        this.totalCount = totalCount;
        this.contentPerPage = contentPerPage;
        this.blocksPerPage = blocksPerPage;
    }

    public String html(long pageIndex) {

        long pages = ((this.totalCount - 1) / contentPerPage) + 1;

        long startNum = ((pageIndex - 1) / blocksPerPage) * blocksPerPage + 1;

        if (pageIndex <= pages && pageIndex >0) {
            String htmlPages = "<a href='#'>[처음]</a>\n<a href='#'>[다음]</a>\n\n";
            String tempPage = "";
            String end = "\n<a href='#'>[다음]</a>\n<a href='#'>[마지막]</a>";

            for (long idx = startNum; idx < startNum + blocksPerPage; idx++) {

                if (idx == pages) {
                    if (idx == pageIndex) {
                        tempPage += String.format("<a href='#' class='on'>%d</a>\n", idx);
                    } else {
                        tempPage += String.format("<a href='#'>%d</a>\n", idx);
                    }
                    break;
                } else {
                    if (idx != pageIndex) {
                        tempPage += String.format("<a href='#'>%d</a>\n", idx);
                    } else if (idx == pageIndex) {
                        tempPage += String.format("<a href='#' class='on'>%d</a>\n", idx);
                    }
                }
            }

            htmlPages = htmlPages + tempPage + end;

            return htmlPages;
        }

        return "페이지가 존재하지 않습니다";
    }
}

public class Practice3 {
    public static void main(String[] args) {
        long totalCount = 230;
        long contentPerPage = 10;
        long blocksPerPage = 13;
        long pageIndex = 23;
        Pager pager = new Pager(totalCount, contentPerPage,blocksPerPage);

        System.out.println(pager.html(pageIndex));
    }
}
