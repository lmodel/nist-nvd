package example;

/* metamodel_version: 1.12.0 */
/* version: 2.2.4 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A page of the match-string API's results.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NvdCpeMatchResponse  {

  private List<NvdMatchStringItem> matchStrings;
  private String format;
  private ZonedDateTime timestamp;
  private int resultsPerPage;
  private int startIndex;
  private int totalResults;
  private String version;


}